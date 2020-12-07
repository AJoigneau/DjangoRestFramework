from django.contrib.auth.models import User
from rest_framework import serializers

from bookings.models import Player, Booking

class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Player
        fields = ('url', 'id', 'first_name', 'last_name', 'email')

class BookingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Booking
        fields = ('url', 'id', 'creation_date', 'booking_date', 'name', 'address', 'player')
