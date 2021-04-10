import logging

from modules.config import Config
from modules.minecraftApi import MinecraftApi
from modules.matrix.matrix import DimensionScheme, ColorScheme

class Core:
	def __init__(self):
		self.config = Config("./config.json")

		logging.basicConfig(format=f"[%(levelname)s] [%(asctime)s] [%(name)s]: %(message)s", level=logging.INFO, handlers=[logging.FileHandler(self.config.logFile), logging.StreamHandler()])
		self.logger = logging.getLogger(self.__class__.__name__)

		self.minecraftApi = MinecraftApi(self.config)

		if self.config.matrix.colorScheme == ColorScheme.MONOCHROME:
			if self.config.matrix.dimensionScheme == DimensionScheme._2D:
				from modules.matrix.matrixMonochrome2D import MatrixMonochrome2D
				self.matrix = MatrixMonochrome2D(self.config, self._set)

			elif self.config.matrix.dimensionScheme == DimensionScheme._3D:
				from modules.matrix.matrixMonochrome3D import MatrixMonochrome3D
				self.matrix = MatrixMonochrome3D(self.config, self._set)

			else:
				self.logger.error(f"Unknown dimension scheme specified in the config ({self.config.matrix.dimensionScheme}). Stopping..")
				exit()

		elif self.config.matrix.colorScheme == ColorScheme.MONOCHROME:
			if self.config.matrix.dimensionScheme == DimensionScheme._2D:
				from modules.matrix.matrixBlocks2D import MatrixBlocks2D
				self.matrix = MatrixBlocks2D(self.config, self._set)

			elif self.config.matrix.dimensionScheme == DimensionScheme._3D:
				from modules.matrix.matrixBlocks3D import MatrixBlocks3D
				self.matrix = MatrixBlocks3D(self.config, self._set)

			else:
				self.logger.error(f"Unknown dimension scheme specified in the config ({self.config.matrix.dimensionScheme}). Stopping..")
				exit()

		else:
			self.logger.error(f"Unknown color scheme specified in the config ({self.config.matrix.colorScheme}). Stopping..")
			exit()

	def _set(self, minecraftCoords, block):
		return self.minecraftApi.setBlock(*minecraftCoords, block)

	def start(self):
		self.minecraftApi.connect()

	def testMatrix(self):
		for y in range(16):
			for x in range(16):
				self.matrix.set((x, y), True)