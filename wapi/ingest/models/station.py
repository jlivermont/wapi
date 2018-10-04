from django.db import models
from django.utils import timezone

class Station(models.Model):
    station_id = models.CharField(max_length=64, unique=True, editable=False)
    name = models.CharField(max_length=200)
    min_date = models.DateField()
    max_date = models.DateField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    data_coverage = models.FloatField()
    elevation = models.FloatField()
    elevation_unit = models.CharField(max_length=24)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "{0} [ID: {1}]".format(self.name, self.station_id)
