import logging

from modules.config import Config
from modules.minecraftApi import MinecraftApi

class CraftMatrix:
	def __init__(self):
		self.config = Config(logging, "./config.json")

		logging.basicConfig(format=f"[%(name)s] [%(asctime)s] [{self.__class__.__name__}]", level=self.config.logLevel, filename=self.config.logFile)

		self.minecraftApi = MinecraftApi(self.config.rconHost, self.config.rconPort, self.config.rconPassword, )