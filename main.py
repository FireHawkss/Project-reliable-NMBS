from gtfs_functions import Feed

gtfs_path = 'rail-tramizmir-gtfs.zip'

feed = Feed(gtfs_path, time_windows=[0, 6, 10, 12, 16, 19, 24])

routes = feed.routes
routes.head(2)