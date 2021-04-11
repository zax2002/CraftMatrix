class Queue:
	def __init__(self):
		self.queue = []

	def add(self, command):
		self.queue.append(command)

	def getAll(self):
		_queue = [*self.queue]
		self.queue = []

		return _queue