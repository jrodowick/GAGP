from django.db import models
# import requests

# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length = 100, primary_key=True)
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
    event_location = models.ForeignKey(Location, on_delete=models.CASCADE)
