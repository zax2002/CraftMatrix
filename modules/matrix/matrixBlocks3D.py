from modules.matrix.matrix import Matrix
from modules.matrix.matrixBlocks import MatrixBlocks
from modules.matrix.matrix3D import Matrix3D

class MatrixBlocks3D(Matrix, MatrixBlocks, Matrix3D):
	def __init__(self, config, setCallback):
		Matrix.__init__(self, config)
		MatrixMonochrome.__init__(self, config, setCallback, clrCallback)
		Matrix2D.__init__(self, config)