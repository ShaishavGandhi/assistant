from wit import Wit
from responses.response import ResponseCreator
from weather.weather import Weather
from utils.format import FormatUtils
from maps.map import Map
from search.search import Wolfram
import apiai
import json

class AIHelper(object):

	access_token = "L44BYDXHQAP2DSB6E2HKTNLZGTFMHTBL"
	ai_access_token = "ecdea114b2d341a68c3e5a11c5ab4a31"
	intent_weather = "weather"
	intent_directions = "directions"
	intent_search = "search"
	responseCreator = None

	def __init__(self):
		self.responseCreator = ResponseCreator();
		self.ai = apiai.ApiAI(self.ai_access_token)

	def query(self, query):
		request = self.ai.text_request()
		request.query = query
		resp = request.getresponse().read()
		print resp
		resp_dict = json.loads(resp)
		self.classify(resp_dict)

	def classify(self, entities):
		entities = entities["result"]
		if "metadata" in entities.keys():
			intent = entities["metadata"]["intentName"]
			confidence = entities["score"]
		# else:
		# 	query = entities["wolfram_search_query"][0]["value"]
		# 	self.executeSearch(query)
		# 	return

		if intent == self.intent_weather:
			location = entities["parameters"]["geo-city"]
			formattedDate = None
			if entities["parameters"]["date"] != "":
				date = entities["parameters"]["date"]# type : 2017-01-07T00:00:00.000-08:00
				formattedDate = FormatUtils().getFormattedDate(date)
			self.executeWeather(location, formattedDate)

		if intent == self.intent_directions:
			destination = entities["parameters"]["address"]
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
		parameters = (
		('podtitle', 'Wikipedia summary')
		)
		response = Wolfram().query(query, parameters)
		if response == None:
			response = "Sorry, I couldn't find the answer to that!"
		self.responseCreator.createSearchResponse(response)
