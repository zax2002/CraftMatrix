import logging
from mcrcon import MCRcon, MCRconException

class MinecraftApi:
	def __init__(self, logger, config):
		self.config = config

		logging.basicConfig(format=f"[%(name)s] [%(asctime)s] [{self.__class__.__name__}]", level=self.config.logLevel, filename=self.config.logFile)

		self.rconIp = self.config.rconIp
		self.rconHost = self.config.rconPort
		self.rconPassword = self.config.rconPassword

		self.rcon = MCRcon(host=self.rconHost, port=self.rconPort, password=self.rconPassword)
		self.connected = False

		self.world = self.config.world

	def start(self):
		self.connect()

	def connect(self):
		try:
			logging.info(f"Connecting to {self.rconHost}:{self.rconPassword}")
			self.rcon.connect()
			self.connected = True

		except MCRconException as e:
			if e.messsage == "Login failed":
				logging.error("Login failed. Stopping..")
				exit()

		except ConnectionRefusedError:
			self.connected = False
			logging.error(f"The connection could not be made as the server actively refused it.")

			self.reconnect()

		except ConnectionError as e:
			self.connected = False
			logging.error(f"Connection error: {e}")

	def reconnect(self):
		logging.info(f"Reconnecting in {self.config.rconReconnectInterval} seconds..")

		time.sleep(self.config.rconReconnectInterval)
		self.connect()

	def setBlock(self, x, y, z, block, successCallback, nbt=""):
		if not self.connected:
			return False

		if self.world == "world":
			command = f"/setblock {x} {y} {z} {block}" + f" {nbt}" if len(nbt) else ""
		else:
			command = f"/execute in {self.world} run setblock {x} {y} {z} {block}" + f" {nbt}" if len(nbt) else ""


		try:
			result = self.rcon.command(command)

			return result == "Changes blocks at the specified position."

		except (ConnectionResetError, ConnectionAbortedError):
			self.connected = False
			logging.error(f"The connection was terminated")

			self.reconnect()