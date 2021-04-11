from django.contrib.auth.models import Booking
from rest_framework import serializers


class BookingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'start_time', 'end_time', 'description']