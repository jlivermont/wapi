from django.conf import settings
from appconf import AppConf

class IngestAppConf(AppConf):
    NOAA_API_KEY1 = 'gWhIPKOZORzepPsoiQIniNgEOTXXpipM'

    NOAA_BASE_URL = 'https://www.ncdc.noaa.gov/cdo-web/api/v2'
    NOAA_SD_STATIONS_URL = '{0}/stations?locationid=FIPS:46'.format(NOAA_BASE_URL)

    class Meta:
        prefix = 'ingest'
        proxy = True
