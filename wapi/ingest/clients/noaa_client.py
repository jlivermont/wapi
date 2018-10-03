import requests

from wapi.ingest.conf import settings

class NOAAClient:
    def _get_common_headers(self):
        return { "token": settings.INGEST_NOAA_API_KEY1 }

    def get_stations(self):
        url = settings.INGEST_NOAA_SD_STATIONS_URL
        headers = self._get_common_headers()
        response = requests.get(url=url, headers=headers)
        print(response.json())
