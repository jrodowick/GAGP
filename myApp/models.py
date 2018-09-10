from django.db import models
from geoposition.fields import GeopositionField


# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length = 100)
    address = models.CharField(max_length = 50)
    city = models.CharField(max_length = 25)
    zip = models.IntegerField()
    position = GeopositionField()
