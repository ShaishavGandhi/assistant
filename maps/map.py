import googlemaps

class Map(object):

    api_key = "AIzaSyAlSia7m6BKWuMI4_JPEwxCN93dQ3nMvPw"
    gmaps = None

    def __init__(self):
        self.gmaps = googlemaps.Client(key=self.api_key)

    def getTimeTo(self, origin, destination):
        directions_result = self.gmaps.directions(origin, destination)
        duration = directions_result[0]["legs"][0]["duration"]["text"]
        distance = directions_result[0]["legs"][0]["distance"]["text"]
        map_dict = {}
        map_dict["duration"] = str(duration)
        map_dict["distance"] = str(distance)
        map_dict["destination"] = str(destination)
        return map_dict
