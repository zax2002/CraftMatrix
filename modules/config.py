import json

class Config:
	def __init__(self, logger, file):
		self.file = file

		try:
			with open(self.file, "r") as f:
				config = json.loads(f.read())

				for key, value in config.items():
					if type(value) == dict:
						section = ConfigSection()
						
						for sectionKey, sectionValue in value:
							section.__setattr__(sectionKey, sectionValue)

						value = section

					self.__setattr__(key, value)

		except FileNotFoundError as e:
			print("Config file not found")
			exit()

		except json.decoder.JSONDecodeError as e:
			print(f"JSON decode error: {e}")
			exit()

class ConfigSection:
	pass