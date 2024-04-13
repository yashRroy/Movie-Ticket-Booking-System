from django.db import models
from datetime import datetime, timezone
from django.contrib.auth.models import User
from django.forms import ValidationError


class Movie(models.Model):
    title = models.CharField(max_length=255, unique=True)
    director = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    release_date = models.DateField()
    duration = models.PositiveIntegerField()
    synopsis = models.TextField()

    def __str__(self):
        return self.title

class Theater(models.Model):
    name = models.CharField(max_length=255, unique=True)
    location = models.CharField(max_length=255)
    capacity = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Showtime(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    theater = models.ForeignKey(Theater, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    available_seats = models.PositiveIntegerField()

    def clean(self):
        if self.date_time < datetime.now(timezone.utc):
            raise ValidationError("Showtime date and time must be in the future.")
        
        if self.available_seats < 0:
            raise ValidationError("Available seats cannot be negative.")
        
        if self.available_seats > self.theater.capacity:
            raise ValidationError("Available seats cannot exceed theater capacity.")
    

    def __str__(self):
        return f"{self.movie.title} - {self.theater.name} ({self.date_time})"
    
class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    showtime = models.ForeignKey(Showtime, on_delete=models.CASCADE)
    seats_reserved = models.PositiveIntegerField()

    def clean(self):
        if self.seats_reserved < 0:
            raise ValidationError("Seats reserved cannot be negative.")
        if self.seats_reserved > self.showtime.available_seats:
            raise ValidationError("Seats reserved cannot exceed available seats.")
        
    def __str__(self):
        return f"Reservation for {self.showtime.movie.title} at {self.showtime.theater.name} on {self.showtime.date_time}"
    
class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    payment_status = models.CharField(max_length=100)

    def clean(self):
        # Validate payment_status against a predefined set of values
        valid_statuses = ['Pending', 'Completed', 'Failed']
        if self.payment_status not in valid_statuses:
            raise ValidationError("Invalid payment status.")
    
    def __str__(self):
        return f"Purchase for {self.reservation.showtime.movie.title} at {self.reservation.showtime.theater.name} on {self.reservation.showtime.date_time}"
