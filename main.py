from gtfs_functions import Feed


gtfs_path = 'rail-tramizmir-gtfs.zip'

feed = Feed(gtfs_path, time_windows=[0, 6, 10, 12, 16, 19, 24])


for entity in feed.entity:
  if entity.HasField('trip_update'):
    print(entity.trip_update)
    print("     SHITE       ")

#parsed_calendar = Feed(gtfs_path).parse_calendar()

#routes = feed.routes
#trips = feed.trips
#stops = feed.stopspip install --upgrade gtfs-realtime-bindings
#stop_times = feed.stop_times
#shapes = feed.shapes

#print(routes)
#print(stops)
#print(parsed_calendar)