import logging

from modules.minecraft.commandsCombiner import CommandsCombiner

class MinecraftUtils:
	def __init__(self, config, rconManager):
		self.logger = logging.getLogger(self.__class__.__name__)

		self.config = config
		self.world = self.config.minecraft.world
		self.minecartsStackCoordinates = self.config.minecraft.minecartsStackCoordinates

		self.rconManager = rconManager
		self.commandsCombiner = CommandsCombiner(self.config)

	def runCommandInWorld(self, command):
		if self.world != "":
			command = f"execute in {self.world} run {command}"

		return self.rconManager.sendCommand(command)

	def setBlock(self, x, y, z, block, nbt=""):
		command = self.getSetBlockCommand(x, y, z, block, nbt)
		result = self.runCommandInWorld(command)

		return result and (result.startswith("Changed the block at") or result.startswith("Could not set the block"))

	def getSetBlockCommand(self, x, y, z, block, nbt=""):
		return f"setblock {x} {y} {z} {block}" + (f" {nbt}" if len(nbt) else "")

		
	def fill(self, x1, y1, z1, x2, y2, z2, block):
		command = f"fill {x1} {y1} {z1} {x2} {y2} {z2} {block}"
		result = self.runCommandInWorld(command)

		return result and (result.startswith("Successfully filled") or result.startswith("No blocks were filled"))

	def runMultipleCommands(self, commands):
		for combinedCommand in self.commandsCombiner.combine(commands, (16+len(self.world) if self.world != "" else 0)):
			self.runCommandInWorld(combinedCommand)