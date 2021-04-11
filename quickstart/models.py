from django.db import models

# Create your models here.
class Booking(models.Model):
    id = models.CharField(max_length=10)
    start_time = models.DateTimeField('start_time')
    end_time = models.DateTimeField('end time')
    description = models.CharField(max_length=200)