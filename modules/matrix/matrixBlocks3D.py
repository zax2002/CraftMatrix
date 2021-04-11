from modules.matrix.matrix import Matrix
from modules.matrix.matrixBlocks import MatrixBlocks
from modules.matrix.matrix3D import Matrix3D

class MatrixBlocks3D(Matrix, MatrixBlocks, Matrix3D):
	def __init__(self, config, setCallback, fillCallback):
		Matrix.__init__(self, config, setCallback, fillCallback)
		MatrixBlocks.__init__(self, config)
		Matrix3D.__init__(self, config)

	def clear(self):
		self.fill((0, 0, 0), (self.xSize-1, self.ySize-1, self.zSize-1), "air")