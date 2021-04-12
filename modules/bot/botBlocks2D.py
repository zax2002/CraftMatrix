from modules.bot.bot import Bot
from modules.bot.botBlocks import BotBlocks

class BotBlocks2D(Bot, BotBlocks):
	def __init__(self, config, setCallback):
		Bot.__init__(self, config, setCallback)
		BotBlocks.__init__(self)

		self.listMode = self.config.colorSchemeBlocks.listMode
		self.list = self.config.colorSchemeBlocks.list

	def _parseCoordinatesAndValue(self, args):
		if len(args) != 3:
			return False, None, None

		*coordinates, block = args

		try:
			for i in range(len(coordinates)):
				coordinates[i] = int(coordinates[i])
		except ValueError:
			return False, None, None

		match = self.regexp.findall(block)
		if len(match) == 0:
			return False, None, None
		
		_, blockId, blockData, _ = match[0]

		if (self.listMode == -1 and blockId not in self.list) or (self.listMode == 1 and blockId in self.list):
			if blockId not in self.list:
				return False, None, None

		return True, coordinates, block