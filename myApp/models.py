from django.db import models
# import requests

# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length = 100)
    address = models.CharField(max_length = 50)
    city = models.CharField(max_length = 25)
    zip = models.IntegerField()

    # def __str__(self):
    #     return self.address

    def asDict(self):
        return {
            'name': self.name,
            'address': self.address,
            'city': self.city,
            'zip': self.zip,
        }
