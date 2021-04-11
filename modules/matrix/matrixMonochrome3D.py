from modules.matrix.matrix import Matrix
from modules.matrix.matrixMonochrome import MatrixMonochrome
from modules.matrix.matrix3D import Matrix3D

class MatrixMonochrome3D(Matrix, MatrixMonochrome, Matrix3D):
	def __init__(self, config, setCallback, fillCallback):
		Matrix.__init__(self, config, setCallback, fillCallback)
		MatrixMonochrome.__init__(self, config)
		Matrix3D.__init__(self, config)

	def clear(self):
		self.fill((0, 0, 0), (self.xSize-1, self.ySize-1, self.zSize-1), 0)