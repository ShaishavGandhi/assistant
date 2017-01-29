import tungsten

class Wolfram(object):

    app_id = "V9XL3G-LGEUTAX9YK"
    client = None

    def __init__(self):
        self.client = tungsten.Tungsten(self.app_id)

    def query(self, query):
        params = {'parsetimeout' : 10}
        # params = {"podtitle" : "Result", "podtitle" : "Latest recorded weather*"}
        res = self.client.query(query, params)
        if res.pods == 0:
            return None
        for pod in res.pods:
            print "Title : " + pod.title
            if pod.format["plaintext"][0] != None:
                print pod.format["plaintext"][0] + " : " + pod.title
            if pod.title == "Result":
                return pod.format["plaintext"][0]
            elif pod.id == "InstantaneousWeather:WeatherData":
                return pod.format["plaintext"][0]
            elif pod.title == "Definition":
                return pod.format["plaintext"][0]
