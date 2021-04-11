from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import Booming
from rest_framework import viewsets
from rest_framework import permissions
from tutorial.quickstart.serializers import BookingSerializer


class BookingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Booking.objects.all().order_by('-date_joined')
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]