import time
import logging
from mcrcon import MCRcon, MCRconException

class RconManager:
	def __init__(self, config):
		self.logger = logging.getLogger(self.__class__.__name__)

		self.config = config

		self.rconHost = self.config.rcon.host
		self.rconPort = self.config.rcon.port
		self.rconPassword = self.config.rcon.password

		self.rcon = MCRcon(host=self.rconHost, port=self.rconPort, password=self.rconPassword)
		self.connected = False

	def connect(self, reconnect=False):
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

			if not reconnect:
				self._reconnect()

		except ConnectionError as e:
			self.connected = False
			self.logger.error(f"Connection error: {e}")

	def _reconnect(self):
		while not self.connected:
			self.logger.info(f"Reconnecting in {self.config.rcon.reconnectInterval} seconds..")

			time.sleep(self.config.rcon.reconnectInterval)
			self.connect(True)

	def sendCommand(self, command):
		if not self.connected:
			self._reconnect()

		try:
			result = self.rcon.command(command)
			self.logger.debug(f"{command}\n{result}")

		except (ConnectionResetError, ConnectionAbortedError):
			self.connected = False
			self.logger.error(f"The connection was terminated")

		except TimeoutError:
			self.connected = False
			self.logger.error(f"Connection timeout")

		finally:
			if not self.connected:
				self._reconnect()
				result = self.sendCommand(command)

		return result