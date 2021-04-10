from modules.matrix.matrix import Matrix
from modules.matrix.matrixBlocks import MatrixBlocks
from modules.matrix.matrix2D import Matrix2D

class MatrixBlocks2D(Matrix, MatrixBlocks, Matrix2D):
	def __init__(self, config, setCallback):
		Matrix.__init__(self, config)
		MatrixMonochrome.__init__(self, config, setCallback, clrCallback)
		Matrix2D.__init__(self, config)