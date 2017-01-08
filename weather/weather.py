import pyowm
from time import mktime
from datetime import datetime

class Weather(object):

	access_token = "377b71700b9269b9de033a45dcaf225d"

	def __init__(self):
		self.client = pyowm.OWM(self.access_token)

	def getWeather(self, location, date):
		#weather = self.client.weather_at_place(location).get_weather()
		if date == None:
			date = datetime.now()
		forecast = self.client.daily_forecast(location)
		date = date.replace(hour=23, minute=59)
		weather = forecast.get_weather_at(int(mktime(date.timetuple())))
		return weather
