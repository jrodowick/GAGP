from django.db import models
from django.contrib.auth.models import User

# import requests

# Create your models here.

EVENT_CHOICES = (
    ('Soccer', "Soccer"),
    ('Football', "Football"),
    ('Baseball', "Baseball"),
    ('Wiffleball', "Wiffleball"),
    ('Ultimate Frisbee', "Ultimate Frisbee"),
    ('Basketball', "Basketball"),
    ('Disc Golf', "Disc Golf"),
    ('Kickball', "Kickball"),
)

class Location(models.Model):
    name = models.CharField(max_length = 80)
    address = models.CharField(max_length = 50)
    city = models.CharField(max_length = 25)
    zip = models.IntegerField()

    def __str__(self):
        return self.name

    def asDict(self):
        return {
            'name': self.name,
            'address': self.address,
            'city': self.city,
            'zip': self.zip,
        }

class Event(models.Model):
    name = models.CharField(max_length = 50)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add = True)
    date_of_event = models.DateField(blank = False)
    time_of_event = models.TimeField(blank = False)
    activity = models.CharField(choices = EVENT_CHOICES, max_length = 50)
    created_by = models.ForeignKey(User, default = None, on_delete = models.CASCADE)

    def __str__(self):
        return self.name

    def asDict(self):
        return {
            'name': self.name,
            'location': self.location,
            'date_created': self.date_created,
            'date_of_event': self.date_of_event,
            'time_of_event': self.time_of_event,
            'activity': self.activity,
        }
