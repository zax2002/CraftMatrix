from modules.bot.bot import Bot
from modules.botBlocks.bot import BotBlocks

class BotBlocks3D(Bot, BotBlocks):
	def __init__(self, config, setCallback):
		Bot.__init__(self, config, setCallback)
		BotBlocks.__init__(self)