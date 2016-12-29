import pyowm

class Weather(object):

	access_token = "377b71700b9269b9de033a45dcaf225d"

	def __init__(self):
		self.client = pyowm.OWM(self.access_token)

	def getWeather(self, location, date):
		weather = self.client.weather_at_place(location).get_weather()
		return weather
