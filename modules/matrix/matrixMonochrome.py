class MatrixMonochrome:
	def __init__(self, config):
		self.onStateBlock = self.config.matrix.colorSchemeMonochrome.onStateBlock
		self.offStateBlock = self.config.matrix.colorSchemeMonochrome.offStateBlock

	def set(self, matrixCoordinates, value):
		matrixCoordinates = tuple(matrixCoordinates)

		if not self._coordinatesInMatrix(matrixCoordinates):
			return

		if matrixCoordinates in self.data and self.data[matrixCoordinates] == value:
			return

		minecraftCoordinates = self._convertCoordinates(matrixCoordinates)

		self.data[matrixCoordinates] = value
		self.setCallback(minecraftCoordinates, self.onStateBlock if value else self.offStateBlock)

	def fill(self, matrixCoordinatesFrom, matrixCoordinatesTo, value):
		matrixCoordinatesFrom = self._cropCoordinates(matrixCoordinatesFrom)
		matrixCoordinatesTo = self._cropCoordinates(matrixCoordinatesTo)
		
		minecraftCoordinatesFrom = self._convertCoordinates(matrixCoordinatesFrom)
		minecraftCoordinatesTo = self._convertCoordinates(matrixCoordinatesTo)

		for y in range(matrixCoordinatesFrom[1], matrixCoordinatesTo[1]+1):
			for x in range(matrixCoordinatesFrom[0], matrixCoordinatesTo[1]+1):
				self.data[(x, y)] = value
		
		self.fillCallback(*minecraftCoordinatesFrom, *minecraftCoordinatesTo, self.onStateBlock if value else self.offStateBlock)
			