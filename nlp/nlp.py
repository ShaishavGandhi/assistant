from wit import Wit
from responses.response import ResponseCreator
from weather.weather import Weather
from utils.format import FormatUtils
from maps.map import Map

class WitHelper(object):

	access_token = "L44BYDXHQAP2DSB6E2HKTNLZGTFMHTBL"
	intent_weather = "weather"
	intent_directions = "directions"

	def send(request, response):
		print('Sending to user...', response['text'])

	def my_action(request):
		print('Received from user...', request['text'])

	actions = {
		'send': send,
		'my_action': my_action,
	}

	def __init__(self):
		self.client = Wit(access_token = self.access_token, actions = self.actions)

	def query(self, query):
		resp = self.client.message(query)
		self.classify(resp["entities"])

	def classify(self, entities):
		print entities
		intent = entities["intent"][0]["value"]
		confidence = entities["intent"][0]["confidence"]

		if intent == self.intent_weather:
			location = entities["location"][0]["value"]
			formattedDate = None
			if "datetime" in entities.keys():
				date = entities["datetime"][0]["values"][0]["value"] # type : 2017-01-07T00:00:00.000-08:00
				formattedDate = FormatUtils().getFormattedDate(date)
			self.executeWeather(location, formattedDate)

		if intent == self.intent_directions:
			destination = entities["location"][0]["value"]
			self.executeDirections(None, destination)


	def executeWeather(self, location, date):
		weather = Weather()
		temp = weather.getWeather(location, date)
		responseCreator = ResponseCreator()
		responseCreator.createWeatherResponse(location, temp)

	def executeDirections(self, origin, destination):
		map = Map()
		map_dict = map.getTimeTo("4 Charlton Court", destination)
		responseCreator = ResponseCreator()
		responseCreator.createMapResponse(map_dict)
