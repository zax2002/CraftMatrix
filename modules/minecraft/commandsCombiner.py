import random
import string

class CommandsCombiner:
	RCON_MAX_COMMAND_LENGTH = 1426

	def __init__(self, config):
		self.config = config

		self.minecartsStackCoordinates = self.config.minecraft.minecartsStackCoordinates
		self.world = self.config.minecraft.world

	def combine(self, commands, addition=0):
		# 141 + len(x) + len(y) + len(z) +
		# len(cmd1) +
		# len(cmd2) +
		# len(cmd3) +
		# len(cmd4) +
		# 40 * (len(cmds)-1)
		# (len(cmds) - 2 if len(cmds) > 2 else 0)

		commands = list(commands)

		combinedCommands = []
		
		while len(commands):
			lenCommands = len(commands)

			if lenCommands == 1:
				combinedCommands.append(commands[0])
				break

			combinedCommandLength = addition + 90 + (-2 if lenCommands > 2 else 0) + len(str(self.minecartsStackCoordinates[0])) + len(str(self.minecartsStackCoordinates[1])) + len(str(self.minecartsStackCoordinates[2]))
			commandsToCombine = []
			while len(commands):
				command = commands.pop(0)
				combinedCommandLength += len(command) + 55

				if combinedCommandLength > self.RCON_MAX_COMMAND_LENGTH:
					commands.insert(0, command)
					break

				commandsToCombine.append(command)

			combinedCommands.append(self._combine(commandsToCombine))

		return combinedCommands

	def _combine(self, commands):
		tag = self._randomTag()

		minecarts = []

		for command in commands:
			nbt = [f'Tags:[{tag}]', f'Command:"{command}"']
			minecarts.append(("command_block_minecart", nbt))

		minecarts.append(("command_block_minecart", [f'Tags:[{tag}]', f'Command:"kill @e[tag={tag}]"'] ))

		firstMinecart = minecarts.pop(0)

		combinedEntity = self._addPassengers(firstMinecart, minecarts)

		return f'summon {combinedEntity[0]} {self.minecartsStackCoordinates[0]} {self.minecartsStackCoordinates[1]} {self.minecartsStackCoordinates[2]} {{{",".join(combinedEntity[1])}}}'

	def _addPassengers(self, rootEntity, passengerEntities):
		passengers = []

		for passengerEntityId, passengerEntityRootNbt in passengerEntities:
			passengerEntityRootNbt.append(f'id:"{passengerEntityId}"')
			passengers.append(f'{{{",".join(passengerEntityRootNbt)}}}')

		rootEntity[1].append(f"Passengers:[{','.join(passengers)}]")

		return rootEntity

	def _randomTag(self):
		return "".join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=5))