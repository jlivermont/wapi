import kronos

from wapi.ingest.clients import noaa_client

@kronos.register('* * * * * ')
def import_stations():
    print("Executing import_stations...")
    noaa_client.NOAAClient().get_stations()
