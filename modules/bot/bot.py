from telegram.ext import Updater, CommandHandler

from modules.bot.cooldownManager import CooldownManager
from modules.matrix.matrix import ColorScheme, DimensionScheme

class Bot:
	def __init__(self, config, setCallback):
		self.config = config

		self.enabledCooldown = self.config.bot.sendCooldown > 0 or self.config.bot.editCooldown > 0
		self.colorScheme = self.config.matrix.colorScheme
		self.dimensionScheme = self.config.matrix.dimensionScheme

		self.setCallback = setCallback

		if self.enabledCooldown:
			self.cooldownManager = CooldownManager(self.config)

		self.updater = Updater(self.config.bot.token)
		self.bot = self.updater.bot
		self.dispatcher = self.updater.dispatcher

	def start(self):
		if self.config.bot.setBotCommandsOnStart:
			self._setCommands()

		self.updater.start_polling()
		self.updater.idle()