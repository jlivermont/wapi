import datetime
import pytest

from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError

from wapi.ingest.models import Station
from wapi.ingest.tests.factories import StationFactory

@pytest.mark.django_db
def test_create_station():
    station = StationFactory()
    assert isinstance(station, Station) is True
    assert station.station_id == 'TEST:001'
    assert station.name == 'test-station'
    assert isinstance(station.created, datetime.datetime) is True


@pytest.mark.django_db
@pytest.mark.parametrize("field", [
    ("station_id"),
    ("name"),
    ("min_date"),
    ("max_date"),
    ("latitude"),
    ("longitude"),
    ("data_coverage"),
    ("elevation"),
    ("elevation_unit"),
])
def test_missing_field_raises_error(field):
    kwargs = {field: None}
    with pytest.raises(IntegrityError):
        StationFactory(**kwargs)


@pytest.mark.django_db
@pytest.mark.parametrize("field,value,error", [
    ("min_date", 3, TypeError),
    ("max_date", "foobar", ValidationError),
    ("latitude", "foobar", ValueError),
    ("longitude", "foobar", ValueError),
    ("data_coverage", "foobar", ValueError),
    ("elevation", "foobar", ValueError),
])
def test_invalid_field_type_raises_error(field, value, error):
    kwargs = {field: value}
    with pytest.raises(error):
        StationFactory(**kwargs)
