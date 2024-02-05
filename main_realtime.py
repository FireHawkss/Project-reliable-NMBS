from google.transit import gtfs_realtime_pb2
import requests

feed = gtfs_realtime_pb2.FeedMessage()
response = requests.get('https://sncb-opendata.hafas.de/gtfs/realtime/c21ac6758dd25af84cca5b707f3cb3de')
feed.ParseFromString(response.content)
for entity in feed.entity:
  if entity.HasField('trip_update'):
    print(entity.trip_update)
    print("     SHITE       ")

print(feed.entity)