from typing import Tuple, List, Dict

import pandas as pd
import folium
import sqlite3
from IPython.display import display # unnevcessary?

pd.set_option('display.precision', 2)

def extract_stops_from_db(db_path: str) -> pd.DataFrame:
    conn = sqlite3.connect(db_path)
    query = "SELECT stop_name, stop_lat, stop_lon FROM stops"
    df = pd.read_sql_query(query, conn)
    conn.close()
    df.columns = ['site', 'latitude', 'longitude']
    return df

# Example usage:
# df_izmir_stops = extract_stops_from_db('izmir_tram_static.db')
# print(df_izmir_stops)

df_tutorial = pd.DataFrame(
    [['hotel',              48.8527, 2.3542],
     ['Sacre Coeur',        48.8867, 2.3431],
     ['Louvre',             48.8607, 2.3376],
     ['Montmartre',         48.8872, 2.3388],
     ['Port de Suffren',    48.8577, 2.2902],
     ['Arc de Triomphe',    48.8739, 2.2950],
     ['Av. Champs Élysées', 48.8710, 2.3036],
     ['Notre Dame',         48.8531, 2.3498],
     ['Tour Eiffel',        48.8585, 2.2945]],
    columns=pd.Index(['site', 'latitude', 'longitude'], name='paris')
)

df_sites = extract_stops_from_db('izmir_tram_static_data.db')

print(df_sites)

avg_location = df_sites[['latitude', 'longitude']].mean() # to display the average location of all stops
map_izmir = folium.Map(location=avg_location, zoom_start=13) 

for site in df_sites.itertuples():
    marker = folium.Marker(location=(site.latitude, site.longitude), tooltip=site.site)
    marker.add_to(map_izmir)

map_izmir