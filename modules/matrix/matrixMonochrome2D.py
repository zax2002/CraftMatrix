from modules.matrix.matrix import Matrix
from modules.matrix.matrixMonochrome import MatrixMonochrome
from modules.matrix.matrix2D import Matrix2D

class MatrixMonochrome2D(Matrix, MatrixMonochrome, Matrix2D):
	def __init__(self, config, setCallback, fillCallback):
		Matrix.__init__(self, config, setCallback, fillCallback)
		MatrixMonochrome.__init__(self, config)
		Matrix2D.__init__(self, config)

	def clear(self):
		self.fill((0, 0), (self.xSize-1, self.ySize-1), 0)