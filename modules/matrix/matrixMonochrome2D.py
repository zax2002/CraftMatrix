from modules.matrix.matrix import Matrix
from modules.matrix.matrixMonochrome import MatrixMonochrome
from modules.matrix.matrix2D import Matrix2D

class MatrixMonochrome2D(Matrix, MatrixMonochrome, Matrix2D):
	def __init__(self, config, setCallback):
		Matrix.__init__(self, config)
		MatrixMonochrome.__init__(self, config, setCallback)
		Matrix2D.__init__(self, config)