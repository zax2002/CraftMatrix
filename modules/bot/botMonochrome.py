from telegram.ext import CommandHandler
from modules.bot.cooldownManager import CooldownAction
import re

class BotMonochrome:
	def __init__(self):
		self.dispatcher.add_handler(CommandHandler("set", self.setCommand))
		self.dispatcher.add_handler(CommandHandler("clr", self.clrCommand))

	def _parseCoordinatesAndValue(self, args):
		if len(args) != 2:
			return False, None, None

		coordinates = args

		try:
			for i in range(len(coordinates)):
				coordinates[i] = int(coordinates[i])
		except ValueError:
			return False, None, None

		return True, coordinates, None

	def setCommand(self, update, context):
		if self.enabledCooldown:
			if not self.cooldownManager.isCooledDown(update.message.from_user.id, CooldownAction.SEND):
				return

		valid, matrixCoordinates, _ = self._parseCoordinatesAndValue(context.args)

		if valid:
			self.setCallback(matrixCoordinates, True)

	def clrCommand(self, update, context):
		if self.enabledCooldown:
			if not self.cooldownManager.isCooledDown(update.message.from_user.id, CooldownAction.SEND):
				return

		valid, matrixCoordinates, _ = self._parseCoordinatesAndValue(context.args)

		if valid:
			self.setCallback(matrixCoordinates, False)