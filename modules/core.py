import logging
import threading
import time

from modules.config import Config
from modules.minecraft.rconManager import RconManager
from modules.minecraft.minecraftUtils import MinecraftUtils
from modules.matrix.matrix import DimensionScheme, ColorScheme

class Core:
	def __init__(self):
		self.config = Config("./config.json")
		self.useCommandsCombiner = self.config.minecraft.useCommandsCombiner

		logging.basicConfig(format=f"[%(levelname)s] [%(asctime)s] [%(name)s]: %(message)s", level=logging.INFO, handlers=[logging.FileHandler(self.config.logFile), logging.StreamHandler()])
		self.logger = logging.getLogger(self.__class__.__name__)

		self.rconManager = RconManager(self.config)
		self.minecraftUtils = MinecraftUtils(self.config, self.rconManager)

		if self.useCommandsCombiner:
			from modules.queue import Queue
			self.queue = Queue()

		if self.config.matrix.colorScheme == ColorScheme.MONOCHROME:
			if self.config.matrix.dimensionScheme == DimensionScheme._2D:
				from modules.matrix.matrixMonochrome2D import MatrixMonochrome2D
				from modules.bot.botMonochrome2D import BotMonochrome2D

				self.matrix = MatrixMonochrome2D(self.config, self._matrixSetCallback, self.minecraftUtils.fill)
				self.bot = BotMonochrome2D(self.config, self._botSetCallback)

			elif self.config.matrix.dimensionScheme == DimensionScheme._3D:
				from modules.matrix.matrixMonochrome3D import MatrixMonochrome3D
				from modules.bot.botMonochrome3D import BotMonochrome3D

				self.matrix = MatrixMonochrome3D(self.config, self._matrixSetCallback, self.minecraftUtils.fill)
				self.bot = BotMonochrome3D(self.config, self._botSetCallback)

			else:
				self.logger.error(f"Unknown dimension scheme specified in the config ({self.config.matrix.dimensionScheme}). Stopping..")
				exit()

		elif self.config.matrix.colorScheme == ColorScheme.BLOCKS:
			if self.config.matrix.dimensionScheme == DimensionScheme._2D:
				from modules.matrix.matrixBlocks2D import MatrixBlocks2D
				from modules.bot.botBlocks2D import BotBlocks2D

				self.matrix = MatrixBlocks2D(self.config, self._matrixSetCallback, self.minecraftUtils.fill)
				self.bot = BotBlocks2D(self.config, self._botSetCallback)

			elif self.config.matrix.dimensionScheme == DimensionScheme._3D:
				from modules.matrix.matrixBlocks3D import MatrixBlocks3D
				from modules.bot.botBlocks3D import BotBlocks3D

				self.matrix = MatrixBlocks3D(self.config, self._matrixSetCallback, self.minecraftUtils.fill)
				self.bot = BotBlocks3D(self.config, self._botSetCallback)

			else:
				self.logger.error(f"Unknown dimension scheme specified in the config ({self.config.matrix.dimensionScheme}). Stopping..")
				exit()

		else:
			self.logger.error(f"Unknown color scheme specified in the config ({self.config.matrix.colorScheme}). Stopping..")
			exit()

	def _matrixSetCallback(self, minecraftCoordinates, block):
		if self.useCommandsCombiner:
			self.queue.add(self.minecraftUtils.getSetBlockCommand(*minecraftCoordinates, block))

		else:
			self.minecraftUtils.setBlock(*minecraftCoordinates, block)

	def _botSetCallback(self, matrixCoordinates, value):
		try:
			self.matrix.set(matrixCoordinates, value)

		except Exception as e:
			print(f"Error: {e}")

	def _checkQueueLoop(self):
		while True:		
			commands = self.queue.getAll()
			self.minecraftUtils.runMultipleCommands(commands)

			if not len(self.queue.queue):
				time.sleep(1)

	def start(self):
		self.rconManager.connect()

		if self.config.matrix.clearOnStart:
			self.matrix.clear()

		for onStartCommand in self.config.minecraft.onStartCommands:
			self.rconManager.sendCommand(onStartCommand % {"world": self.config.minecraft.world})

		if self.useCommandsCombiner:
			thread = threading.Thread(target=self._checkQueueLoop)
			thread.daemon = True
			thread.start()

		self.bot.start()