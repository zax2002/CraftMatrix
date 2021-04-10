class Matrix3D:
	def __init__(self, config):
		self.xDirection = self.config.matrix.dimensionScheme3d.xDirection
		self.yDirection = self.config.matrix.dimensionScheme3d.yDirection
		self.zDirection = self.config.matrix.dimensionScheme3d.zDirection

		self.xSize = self.config.matrix.dimensionScheme3d.xSize
		self.ySize = self.config.matrix.dimensionScheme3d.ySize
		self.zSize = self.config.matrix.dimensionScheme3d.zSize

	def _coordsInMatrix(self, matrixCoords):
		return (
			matrixCoords[0] > 0 and matrixCoords[0] < self.xSize and \
			matrixCoords[1] > 0 and matrixCoords[1] < self.ySize and \
			matrixCoords[2] > 0 and matrixCoords[2] < self.zSize
		)

	def _convertCoords(self, matrixCoords):
		minecraftCoords = (
			self.anchorMinecraftCoords[0] + (
				matrixCoords[0]*self.xDirection[0] +
				matrixCoords[1]*self.yDirection[0] +
				matrixCoords[2]*self.zDirection[0]
			),
			self.anchorMinecraftCoords[1] + (
				matrixCoords[0]*self.xDirection[1] +
				matrixCoords[1]*self.yDirection[1] +
				matrixCoords[2]*self.zDirection[1]
			),
			self.anchorMinecraftCoords[2] + (
				matrixCoords[0]*self.xDirection[2] +
				matrixCoords[1]*self.yDirection[2] +
				matrixCoords[2]*self.zDirection[2]
			)
		)

		return minecraftCoords