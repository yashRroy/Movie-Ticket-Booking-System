from rest_framework import serializers
from .models import Movie, Purchase, Reservation, Theater, Showtime

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class TheaterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theater
        fields = '__all__'

class ShowtimeSerializer(serializers.ModelSerializer):
    movie = MovieSerializer(read_only=True)
    theater = TheaterSerializer(read_only=True)

    class Meta:
        model = Showtime
        fields = '__all__'

class ReservationSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)  # Assuming we want to serialize user's ID only
    showtime = ShowtimeSerializer(read_only=True)  # Nested serializer for Showtime

    class Meta:
        model = Reservation
        fields = '__all__'

class PurchaseSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)  # Assuming we want to serialize user's ID only
    reservation = ReservationSerializer(read_only=True)  # Nested serializer for Reservation
    showtime = ShowtimeSerializer(source='reservation.showtime', read_only=True)

    class Meta:
        model=Purchase
        fields= '__all__'