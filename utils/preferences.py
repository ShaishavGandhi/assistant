
class Preferences(object):

	temperature_unit = "fahrenheit" # default


	def setTemperatureUnit(self, unit):
		self.temperature_unit = unit

    def getTemperatureUnit(self):
        return self.temperature_unit
