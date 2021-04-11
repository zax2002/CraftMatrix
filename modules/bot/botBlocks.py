from telegram.ext import CommandHandler
from modules.bot.cooldownManager import CooldownAction
import re

class BotBlocks:
	def __init__(self):
		self.regexp = re.compile(r"(\w+:|)\w+(\[( *\w+ *= *[a-z0-9\.]+ *,{0,1})+\]|)")

		self.dispatcher.add_handler(CommandHandler("set", self.setCommand))

	def setCommand(self, update, context):
		if update.message != None:
			userId = update.message.from_user.id
			action = CooldownAction.SEND

		elif update.edited_message != None and self.config.bot.allowEdit:
			userId = update.edited_message.from_user.id
			action = CooldownAction.EDIT

		else:
			return

		if self.enabledCooldown:
			if not self.cooldownManager.isCooledDown(userId, action):
				return

		valid, matrixCoordinates, value = self._parseCoordinatesAndValue(context.args)

		if valid:
			self.setCallback(matrixCoordinates, value)