import time

class CooldownAction:
	SEND = 0
	EDIT = 1

class CooldownManager:
	def __init__(self, config):
		self.config = config

		self.cooldown = {
			CooldownAction.SEND: self.config.bot.sendCooldown,
			CooldownAction.EDIT: self.config.bot.editCooldown
		}

		self.users = {}

	def isCooledDown(self, userId, actionType):
		currentTime = time.time()

		if userId in self.users and actionType in self.users[userId] and (currentTime - self.users[userId][actionType]) < self.cooldown[actionType]:
			return False

		else:
			if userId not in self.users:
				self.users[userId] = {}

			self.users[userId][actionType] = currentTime
			
			return True
