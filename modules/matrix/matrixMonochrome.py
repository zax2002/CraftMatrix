class MatrixMonochrome:
	def __init__(self, config, setCallback):
		self.onStateBlock = self.config.matrix.colorSchemeMonochrome.onStateBlock
		self.offStateBlock = self.config.matrix.colorSchemeMonochrome.offStateBlock

		self.setCallback = setCallback

	def set(self, matrixCoords, value):
		matrixCoords = tuple(matrixCoords)

		if not self._coordsInMatrix(matrixCoords):
			return

		if matrixCoords in self.data and self.data[matrixCoords] == value:
			return

		minecraftCoords = self._convertCoords(matrixCoords)

		if self.setCallback(minecraftCoords, self.onStateBlock if value else self.offStateBlock):
			self.data[matrixCoords] = value