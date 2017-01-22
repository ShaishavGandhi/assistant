from wit import Wit
from responses.response import ResponseCreator
from weather.weather import Weather
from utils.format import FormatUtils
from maps.map import Map
from search.search import Wolfram

class WitHelper(object):

	access_token = "NOSL2SXAPZVXSZDDS4I5BDPQVVDHHKLS"
	intent_weather = "weather"
	intent_directions = "directions"
	intent_search = "search"
	responseCreator = None

	def send(request, response):
		print('Sending to user...', response['text'])

	def my_action(request):
		print('Received from user...', request['text'])

	actions = {
		'send': send,
		'my_action': my_action,
	}

	def __init__(self):
		self.responseCreator = ResponseCreator();
		self.client = Wit(access_token = self.access_token, actions = self.actions)

	def query(self, query):
		resp = self.client.message(query)
		self.classify(resp["entities"])

	def classify(self, entities):
		print entities
		if "intent" in entities.keys():
			intent = entities["intent"][0]["value"]
			confidence = entities["intent"][0]["confidence"]
		else:
			query = entities["wolfram_search_query"][0]["value"]
			self.executeSearch(query)
			return

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

		if intent == self.intent_search:
			query = entities["wolfram_search_query"][0]["value"]
			self.executeSearch(query)


	def executeWeather(self, location, date):
		weather = Weather()
		temp = weather.getWeather(location, date)
		self.responseCreator.createWeatherResponse(location, temp)

	def executeDirections(self, origin, destination):
		map = Map()
		map_dict = map.getTimeTo("4 Charlton Court", destination)
		self.responseCreator.createMapResponse(map_dict)

	def executeSearch(self, query):
		response = Wolfram().query(query)
		if response == None:
			response = "Sorry, I couldn't find the answer to that!"
		self.responseCreator.createSearchResponse(response)
