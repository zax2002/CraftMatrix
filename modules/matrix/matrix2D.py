class Matrix2D:
	def __init__(self, config):
		self.xDirection = self.config.matrix.dimensionScheme2d.xDirection
		self.yDirection = self.config.matrix.dimensionScheme2d.yDirection

		self.xSize = self.config.matrix.dimensionScheme2d.xSize
		self.ySize = self.config.matrix.dimensionScheme2d.ySize

	def _coordsInMatrix(self, matrixCoords):
		return (
			matrixCoords[0] > 0 and matrixCoords[0] < self.xSize and \
			matrixCoords[1] > 0 and matrixCoords[1] < self.ySize
		)

	def _convertCoords(self, matrixCoords):
		minecraftCoords = (
			self.anchorMinecraftCoords[0] + (
				matrixCoords[0]*self.xDirection[0] +
				matrixCoords[1]*self.yDirection[0]
			),
			self.anchorMinecraftCoords[1] + (
				matrixCoords[0]*self.xDirection[1] +
				matrixCoords[1]*self.yDirection[1]
			),
			self.anchorMinecraftCoords[2] + (
				matrixCoords[0]*self.xDirection[2] +
				matrixCoords[1]*self.yDirection[2]
			)
		)

		return minecraftCoords