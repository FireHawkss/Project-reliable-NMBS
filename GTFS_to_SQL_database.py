#from gtfs_functions import Feed
import pandas
from sqlalchemy import create_engine
import zipfile
from io import TextIOWrapper

def create_sql_database(dbname,list_of_files, zipName):

    # Specify the SQLite database file path with .db extension
    db_path = dbname+"_static_data.db"
    # Create a SQLite engine
    engine = create_engine(f'sqlite:///{db_path}')
 
    with zipfile.ZipFile(zipName, 'r') as z:
        for file in list_of_files:
            txt_filename = file + ".txt"
            with z.open(txt_filename) as f:
                csv_file = pandas.read_csv(TextIOWrapper(f, encoding='utf-8'))
                # Write the DataFrame to the SQLite database
                csv_file.to_sql(file, engine, index=False, if_exists='replace')


izmir_tram_list_of_files = ['agency','calendar','calendar_dates','routes','stop_times','stops','trips']
izmir_izban_list_of_files = ['agency','calendar','calendar_dates','routes','stop_times','stops','trips']
NMBS_list_of_files = ['agency','calendar','calendar_dates','routes','stop_times','stop_time_overrides','stops','transfers','translations','trips']

#create_sql_database("izmir_tram", izmir_tram_list_of_files)
create_sql_database("izmir_izban", izmir_izban_list_of_files, "rail-izban-gtfs.zip")
#create_sql_database("NMBS", NMBS_list_of_files)

