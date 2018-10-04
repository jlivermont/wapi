import factory

from datetime import (date, datetime)
from dateutil.relativedelta import *

from wapi.ingest.models import Station


class StationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Station

    station_id = 'TEST:001'
    name = 'test-station'
    latitude = 38.8977
    longitude = 77.0365
    max_date = date.today()
    min_date = max_date - relativedelta(year=3)
    data_coverage = 1
    elevation = 1217.3
    elevation_unit = "METERS"
