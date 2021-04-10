class Matrix:
	def __init__(self, config, setCallback, fillCallback):
		self.config = config

		self.setCallback = setCallback
		self.fillCallback = fillCallback

		self.anchorMinecraftCoordinates = config.minecraft.anchorCoordinates

		self.data = {}

class DimensionScheme:
	_2D = 0
	_3D = 1

class ColorScheme:
	MONOCHROME = 0
	BLOCKS = 1