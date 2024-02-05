from gtfs_functions import Feed
import csv
import pandas
from sqlalchemy import create_engine

def create_sql_database(name,list_of_files):

    # Specify the SQLite database file path with .db extension
    db_path = name+"_static_data.db"
    # Create a SQLite engine
    engine = create_engine(f'sqlite:///{db_path}')

    for file in list_of_files:
        csv_file = pandas.read_csv(name + "_unpacked/" + file + ".txt")
        # Write the DataFrame to the SQLite database
        csv_file.to_sql(file, engine, index=False, if_exists='replace')


izmir_list_of_files = ['agency','calendar','calendar_dates','routes','stop_times','stops','trips']
NMBS_list_of_files = ['agency','calendar','calendar_dates','routes','stop_times','stop_time_overrides','stops','transfers','translations','trips']

create_sql_database("izmir_tram", izmir_list_of_files)
create_sql_database("NMBS", NMBS_list_of_files)


#print(test)


gtfs_path = 'rail-tramizmir-gtfs.zip'

#feed = Feed(gtfs_path, time_windows=[0, 6, 10, 12, 16, 19, 24])




#parsed_calendar = Feed(gtfs_path).parse_calendar()

#routes = feed.routes
#trips = feed.trips
#stops = feed.stopspip install --upgrade gtfs-realtime-bindings
#stop_times = feed.stop_times
#shapes = feed.shapes

#print(routes)
#print(stops)
#print(parsed_calendar)