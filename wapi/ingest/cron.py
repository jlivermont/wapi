import kronos

@kronos.register('* * * * * ')
def import_stations():
    print("Executing import_stations...")
