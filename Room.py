class Room:
	"""Class that defines a single chat room, 
	Maintaining a list of the current users"""
	
	def __init__(self, name):
		self.users = []
		self.name = name
		print "Created new room: {}".format(self.name)

	#send the given message to all users in this room
	#accepts: name of the user sending the message, message to send
	def send_message(self, sender, msg):
		for user in self.users:
			if user.name != sender:
				conns.send(sender, user.sock, msg)

	#adds the given user to the list of users
	#accepts: User object to add
	def add_user(self, user):
		if user not in self.users:
			self.users.append(user)

	#remove a user from the room
	def remove_user(self, user):
		if user in self.users:
			self.users.remove(user)

import conns
