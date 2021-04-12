from modules.bot.bot import Bot
from modules.bot.botBlocks import BotBlocks

class BotBlocks3D(Bot, BotBlocks):
	def __init__(self, config, setCallback):
		Bot.__init__(self, config, setCallback)
		BotBlocks.__init__(self)

		self.listMode = self.config.matrix.colorSchemeBlocks.listMode
		self.list = self.config.matrix.colorSchemeBlocks.list

	def _parseCoordinatesAndValue(self, args):
		if len(args) != 4:
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

	def _setCommands(self):
		self.bot.set_my_commands(self.config.bot.botBlocks3DCommands)