class MatrixBlocks:
	def __init__(self, config):
		self.list = self.config.matrix.colorSchemeBlocks.list
		self.listMode = self.config.matrix.colorSchemeBlocks.listMode

	def set(self, matrixCoordinates, block):
		matrixCoordinates = tuple(matrixCoordinates)

		if not self._coordinatesInMatrix(matrixCoordinates):
			return False

		if matrixCoordinates in self.data and self.data[matrixCoordinates] == block:
			return False

		if not self._validateBlock(block):
			return False

		minecraftCoordinates = self._convertCoordinates(matrixCoordinates)

		if self.setCallback(*minecraftCoordinates, block):
			self.data[matrixCoordinates] = block

			return True

		else:
			return True

	def fill(self, matrixCoordinatesFrom, matrixCoordinatesTo, block):
		if not self._validateBlock(block):
			return False

		matrixCoordinatesFrom = self._cropCoordinates(matrixCoordinatesFrom)
		matrixCoordinatesTo = self._cropCoordinates(matrixCoordinatesTo)
		
		minecraftCoordinatesFrom = self._convertCoordinates(matrixCoordinatesFrom)
		minecraftCoordinatesTo = self._convertCoordinates(matrixCoordinatesTo)

		if self.fillCallback(*minecraftCoordinatesFrom, *minecraftCoordinatesTo, block):
			for y in range(matrixCoordinatesFrom[1], matrixCoordinatesTo[1]+1):
				for x in range(matrixCoordinatesFrom[0], matrixCoordinatesTo[1]+1):
					self.data[(x, y)] = block

			return True

		else:
			return False

	def _validateBlock(self, block):
		if self.listMode == ListMode.WHITELIST:
			return block in self.list

		elif self.listMode == ListMode.DISABLED:
			return True

		elif self.listMode == ListMode.BLACKLIST:
			return block not in self.list

		else:
			logging.error(f"Unknown list mode specified in the config ({self.config.matrix.colorSchemeBlocks.listMode}). Stopping..")
			exit()

class ListMode:
	WHITELIST = -1
	DISABLED = 0
	BLACKLIST = 1