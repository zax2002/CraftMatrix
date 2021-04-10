class Matrix2D:
	def __init__(self, config):
		self.xDirection = self.config.matrix.dimensionScheme2d.xDirection
		self.yDirection = self.config.matrix.dimensionScheme2d.yDirection

		self.xSize = self.config.matrix.dimensionScheme2d.xSize
		self.ySize = self.config.matrix.dimensionScheme2d.ySize

	def _coordsInMatrix(self, matrixCoordinates):
		return (
			matrixCoordinates[0] >= 0 and matrixCoordinates[0] < self.xSize and \
			matrixCoordinates[1] >= 0 and matrixCoordinates[1] < self.ySize
		)

	def _convertCoordinates(self, matrixCoordinates):
		minecraftCoordinates = (
			self.anchorMinecraftCoordinates[0] + (
				matrixCoordinates[0]*self.xDirection[0] +
				matrixCoordinates[1]*self.yDirection[0]
			),
			self.anchorMinecraftCoordinates[1] + (
				matrixCoordinates[0]*self.xDirection[1] +
				matrixCoordinates[1]*self.yDirection[1]
			),
			self.anchorMinecraftCoordinates[2] + (
				matrixCoordinates[0]*self.xDirection[2] +
				matrixCoordinates[1]*self.yDirection[2]
			)
		)

		return minecraftCoordinates

	def _cropCoordinates(self, matrixCoordinates):
		matrixCoordinates = list(matrixCoordinates)

		if matrixCoordinates[0] < 0:
			matrixCoordinates[0] = 0
		elif matrixCoordinates[0] >= self.xSize:
			matrixCoordinates[0] = self.xSize-1

		if matrixCoordinates[1] < 0:
			matrixCoordinates[1] = 0
		elif matrixCoordinates[1] >= self.ySize:
			matrixCoordinates[1] = self.ySize-1

		return tuple(matrixCoordinates)