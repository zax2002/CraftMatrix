from modules.bot.bit import Bot
from modules.bot.botBlocks import BotMonochrome

class BotMonochrome3D(Bot, BotMonochrome):
	def __init__(self, config, setCallback):
		Bot.__init__(self, config, setCallback)
		BotMonochrome.__init__(self)