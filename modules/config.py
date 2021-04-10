import json5

class Config:
	def __init__(self, file):
		self.file = file

		try:
			with open(self.file, "r") as f:
				config = json5.loads(f.read())

			self._parseSection(config, self)

		except FileNotFoundError as e:
			print("Config file not found")
			exit()

		except ValueError as e:
			print(f"JSON decode error: {e}")
			exit()

	def _parseSection(self, data, instance):
		for key, value in data.items():
			if type(value) == dict:
				section = ConfigSection()
				self._parseSection(value, section)

				value = section

			instance.__setattr__(key, value)

class ConfigSection:
	pass