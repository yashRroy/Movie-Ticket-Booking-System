from django.contrib import admin
from .models import Movie, Purchase, Reservation, Theater, Showtime

admin.site.register(Movie)
admin.site.register(Theater)
admin.site.register(Showtime)
admin.site.register(Reservation)
admin.site.register(Purchase)



