from modules.bot.bot import Bot
from modules.bot.botBlocks import BotBlocks

class BotBlocks2D(Bot, BotBlocks):
	def __init__(self, config, setCallback):
		Bot.__init__(self, config, setCallback)
		BotBlocks.__init__(self)

	def _parseCoordinatesAndValue(self, args):
		if len(args) != 3:
			return False, None, None

		*coordinates, block = args

		try:
			for i in range(len(coordinates)):
				coordinates[i] = int(coordinates[i])
		except ValueError:
			return False, None, None

		if not self.regexp.match(block):
			return False, None, None

		return True, coordinates, block