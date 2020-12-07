from django.contrib.auth.models import User
from rest_framework import permissions, renderers, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from bookings.models import Player, Booking
from bookings.permissions import IsOwnerOrReadOnly
from bookings.serializers import PlayerSerializer, BookingSerializer

class PlayerViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class BookingViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer