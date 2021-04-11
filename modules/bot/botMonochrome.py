from telegram.ext import CommandHandler
from modules.bot.cooldownManager import CooldownAction
import re

class BotMonochrome:
	def __init__(self):
		self.dispatcher.add_handler(CommandHandler("set", self.setCommand))
		self.dispatcher.add_handler(CommandHandler("clr", self.clrCommand))


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

		valid, matrixCoordinates, _ = self._parseCoordinatesAndValue(context.args)

		if valid:
			self.setCallback(matrixCoordinates, True)

	def clrCommand(self, update, context):
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

		valid, matrixCoordinates, _ = self._parseCoordinatesAndValue(context.args)

		if valid:
			self.setCallback(matrixCoordinates, False)