import time
import logging
from mcrcon import MCRcon, MCRconException

class MinecraftApi:
	def __init__(self, config):
		self.logger = logging.getLogger(self.__class__.__name__)

		self.config = config

		self.rconHost = self.config.rcon.host
		self.rconPort = self.config.rcon.port
		self.rconPassword = self.config.rcon.password

		self.rcon = MCRcon(host=self.rconHost, port=self.rconPort, password=self.rconPassword)
		self.connected = False

		self.world = self.config.minecraft.world

	def connect(self):
		try:
			self.logger.info(f"Connecting to {self.rconHost}:{self.rconPort}..")
			
			self.rcon.connect()
			self.connected = True

			self.logger.info(f"Сonnected successfully")

		except MCRconException as e:
			if e.messsage == "Login failed":
				self.logger.error("Login failed. Stopping..")
				exit()

		except ConnectionRefusedError:
			self.connected = False
			self.logger.error(f"The connection could not be made as the server actively refused it.")

			self._reconnect()

		except ConnectionError as e:
			self.connected = False
			self.logger.error(f"Connection error: {e}")

	def _reconnect(self):
		self.logger.info(f"Reconnecting in {self.config.rcon.reconnectInterval} seconds..")

		time.sleep(self.config.rcon.reconnectInterval)
		self.connect()

	def setBlock(self, x, y, z, block, nbt=""):
		if not self.connected:
			return False

		if self.world == "world":
			command = f"setblock {x} {y} {z} {block}" + (f" {nbt}" if len(nbt) else "")
		else:
			command = f"execute in {self.world} run setblock {x} {y} {z} {block}" + (f" {nbt}" if len(nbt) else "")


		try:
			result = self.rcon.command(command)
			self.logger.debug(f"{command}\n{result}")

			return result.startswith("Changed the block at") or result.startswith("Could not set the block")

		except (ConnectionResetError, ConnectionAbortedError):
			self.connected = False
			self.logger.error(f"The connection was terminated")

			self._reconnect()