from speech.speech import Speech

class ResponseCreator(object):

	def __init__(self):
		#initialize something
		hello = "hello!"

	def createWeatherResponse(self, location, weather):
		temperature = weather.get_temperature('fahrenheit')
		max_temp = int(round(temperature["temp_max"]))
		min_temp = int(round(temperature["temp_min"]))
		average = int(round(temperature["temp"]))
		response = "The weather in " + str(location) + " is an average of " + str(average) + " degrees fahrenheit with maximum of " + str(max_temp) + " degrees and minimum of " + str(min_temp)
		print response
		tts = Speech()
		#tts.speak(response)
