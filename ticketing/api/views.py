from django.shortcuts import render
#auth

# tickets/views.py
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .models import Movie, Purchase, Reservation, Theater, Showtime
from .serializers import MovieSerializer, PurchaseSerializer, ReservationSerializer, TheaterSerializer, ShowtimeSerializer



class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticated]  # Add permissions as needed

class TheaterViewSet(viewsets.ModelViewSet):
    queryset = Theater.objects.all()
    serializer_class = TheaterSerializer
    permission_classes = [IsAuthenticated]  # Add permissions as needed

class ShowtimeViewSet(viewsets.ModelViewSet):
    queryset = Showtime.objects.all()
    serializer_class = ShowtimeSerializer
    permission_classes = [IsAuthenticated]  # Add permissions as needed

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [IsAuthenticated]  

    def get_queryset(self):
        return Reservation.objects.filter(user=self.request.user)

class PurchaseViewSet(viewsets.ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    permission_classes = [IsAuthenticated]  

    def get_queryset(self):
        return Purchase.objects.filter(user=self.request.user)
    

