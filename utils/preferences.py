import json
import shelve

class Preferences(object):

	key_temp = "temperature"
	temperature_unit = "fahrenheit" # default

	def setTemperatureUnit(self, unit):
		local_db = shelve.open('preferences.db')
		try:
			local_db[self.key_temp] = unit
		finally:
			local_db.close()

	def getTemperatureUnit(self):
		local_db = shelve.open('preferences.db')
		temp_unit = self.temperature_unit
		try:
			temp_unit = local_db[self.key_temp]
		finally:
			local_db.close()
		return temp_unit

	def loadPreferences(self, preferences):
		preference_dict = json.loads(preferences)
		if self.key_temp in preference_dict.keys():
			self.setTemperatureUnit(preference_dict[self.key_temp])
