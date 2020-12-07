from rest_framework.test import APIClient
from rest_framework import status
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIRequestFactory

from bookings.models import Booking, Player

class BookingTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url_player = reverse('player-list')
        self.url_player = reverse('booking-list')
        self.player_info = {'first_name': 'Jean', 'last_name': 'Dupond', 'email': 'jean.dupond@example.com'}
        self.booking_info = {'name': 'réservation1', 'address': '3 rue de Paris', 'creation_date': '2020-12-05T18:11:00Z', 'booking_date':'2019-12-05T18:11:00Z'}
        Player.objects.create(first_name='Jean', last_name='Dupond', email='jean.dupond@example.com')
        Booking.objects.create(name='réservation1', address='3 rue de Paris', creation_date='2020-12-05T18:11:00Z', booking_date='2020-12-05T18:11:00Z')

    def test_create_player(self):
        player = {'first_name': 'Pierre', 'last_name': 'Durand', 'email': 'pierre.durand@example.com'}
        self.client.post('/players/', player, format='json')
        response = self.client.get(reverse('player-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Player.objects.all()[1].first_name, player["first_name"])

    def test_update_player(self):
        updated_player = self.player_info
        new_first_name = 'Sébastien'
        updated_player['first_name'] = new_first_name
        response = self.client.put('/players/1/', updated_player)
        self.assertEqual(Player.objects.all()[0].first_name, new_first_name)

    def test_delete_player(self):
        Player.objects.create(first_name='Pierre', last_name='Durand', email='pierre.durand@example.com')
        response = self.client.delete('/players/2/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(len(Player.objects.all()), 1)
        self.assertEqual(Player.objects.all()[0].first_name, self.player_info['first_name'])

    def test_create_booking(self):
        booking = {'name': 'réservation2', 'address': '23 rue des champs', 'creation_date': '2020-12-05T18:11:00Z', 'booking_date':'2019-12-05T18:11:00Z'}
        self.client.post('/bookings/', booking, format='json')
        response = self.client.get(reverse('booking-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Booking.objects.all()[1].name, booking["name"])

    def test_update_booking(self):
        updated_booking = self.booking_info
        new_booking_name = 'Sébastien'
        updated_booking['name'] = new_booking_name
        response = self.client.put('/bookings/1/', updated_booking)
        self.assertEqual(Booking.objects.all()[0].name, new_booking_name)

    def test_delete_booking(self):
        Booking.objects.create(name='réservation2', address='23 rue des champs', creation_date='2020-12-05T18:11:00Z', booking_date='2020-12-05T18:11:00Z')
        response = self.client.delete('/bookings/2/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(len(Booking.objects.all()), 1)
        self.assertEqual(Booking.objects.all()[0].name, self.booking_info['name'])
