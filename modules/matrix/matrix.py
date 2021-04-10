class Matrix:
	def __init__(self, config):
		self.config = config

		self.anchorMinecraftCoords = config.minecraft.anchorCoords

		self.data = {}

class DimensionScheme:
	_2D = 0
	_3D = 1

class ColorScheme:
	MONOCHROME = 0
	BLOCKS = 1