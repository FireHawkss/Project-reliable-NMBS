from gtfslib.dao import Dao
# If db.sqlite exists, use it. Otherwise create a new one.
dao = Dao("data.sqlite")

dao.load_gtfs("rail-tramizmir-gtfs.zip")

