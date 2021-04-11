from modules.bot.bot import Bot
from modules.bot.botMonochrome import BotMonochrome

class BotMonochrome3D(Bot, BotMonochrome):
	def __init__(self, config, setCallback):
		Bot.__init__(self, config, setCallback)
		BotMonochrome.__init__(self)

	def _parseCoordinatesAndValue(self, args):
		if len(args) != 3:
			return False, None, None

		coordinates = args

		try:
			for i in range(len(coordinates)):
				coordinates[i] = int(coordinates[i])
		except ValueError:
			return False, None, None

		return True, coordinates, None