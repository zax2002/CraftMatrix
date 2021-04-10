from modules.bot.bot import Bot
from modules.bot.botMonochrome import BotMonochrome

class BotMonochrome2D(Bot, BotMonochrome):
	def __init__(self, config, setCallback):
		Bot.__init__(self, config, setCallback)
		BotMonochrome.__init__(self)