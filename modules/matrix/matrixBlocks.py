class MatrixBlocks:
	def __init__(self, config, setCallback):
		self.list = self.config.matrix.colorSchemeBlocks.list
		self.listMode = self.config.matrix.colorSchemeBlocks.listMode

		self.setCallback = setCallback

	def set(self, matrixCoords, block):
		matrixCoords = tuple(matrixCoords)

		if not self._coordsInMatrix(matrixCoords):
			return

		if matrixCoords in self.data and self.data[matrixCoords] == value:
			return

		if not self._validateBlock(block):
			return

		minecraftCoords = self._convertCoords(matrixCoords)

		if self.setCallback(minecraftCoords, block):
			self.data[matrixCoords] = block

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