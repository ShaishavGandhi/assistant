from speech.speech import Speech

class ResponseCreator(object):

	def __init__(self):
		#initialize something
		hello = "hello!"

	def createWeatherResponse(self, location, weather):
		temperature = weather.get_temperature('fahrenheit')
		max_temp = int(round(temperature["max"]))
		min_temp = int(round(temperature["min"]))
		average = int(round(temperature["day"]))
		response = "The weather in " + str(location) + " is mainly " + weather.get_detailed_status() + " with an overall temperature of " + str(average) + " degrees fahrenheit with maximum of " + str(max_temp) + " degrees and minimum of " + str(min_temp)
		print response
		tts = Speech()
		tts.speak(response)
