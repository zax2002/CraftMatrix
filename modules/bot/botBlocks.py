from telegram.ext import CommandHandler
from modules.bot.cooldownManager import CooldownAction
import re

class BotBlocks:
	def __init__(self):
		self.regexp = re.compile(r"(\w+:|)\w+(\[( *\w+ *= *[a-z0-9\.]+ *,{0,1})+\])")

		self.dispatcher.add_handler(CommandHandler("set", self.setCommand))

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
			return False

		return True, (x, y), block

	def setCommand(self, update, context):
		if self.enabledCooldown:
			if not self.cooldownManager.isCooledDown(update.message.__getattribute__("from").id, CooldownAction.SEND):
				return

		valid, matrixCoordinates, value = self._parseCoordinatesAndValue(context.args)

		if valid:
			self.setCallback(matrixCoordinates, value)