from google.transit import gtfs_realtime_pb2
import requests
import json

update = []


# Create an instance of the FeedMessage class (empty container to put gtfs-realtime data in)
feed = gtfs_realtime_pb2.FeedMessage()
# gets the raw realtime data from NMBS in protocol buffer (pb) format
response = requests.get('https://sncb-opendata.hafas.de/gtfs/realtime/c21ac6758dd25af84cca5b707f3cb3de')
# parses the pb data from NMBS converts it to string and populates the feed variable with it 
feed.ParseFromString(response.content)
# the only usable info in the FeedMessage class is in a entity which is of a FeedEntity class
# inside the FeedEntity class:
# id is for message transmission |
# there are 3 optional classes but the FeedEntity has to have at least 1 of them. They are 
# trip_update from the class TripUpdate, vehicle from the class VehiclePosition, alert from the class Alert  
# class TripUpdate: 
# property trip from class TripDescriptor --> the trip that this message applies to 
# optional property vehicle from class VehicleDescriptor gives info about the vehicle serving the trip
# the message StopTimeEvent has 3 optional properties:
# delay --> + is delay - is coming early
# time --> time in unix time
# uncertainty --> is = 0 if prediction 100% certain
for entity in feed.entity:
  if entity.HasField('trip_update'):
    update.append(entity.trip_update)


# print(update)
print(update[5])
# print(len(update))
#print(type(update[0]))



# json_container = json.loads(str(update[0]))
# json_str = json.dumps(json_container,indent=2)
# print(json_str)