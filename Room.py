import conns
import User

class Room:
	"""Class that defines a single chat room, 
	Maintaining a list of the current users"""
	users = []
	name = ""
	
	def __init__(self, name):
		self.name = name
		print "Created new room: {}".format(self.name)

	#send the given message to all users in this room
	#accepts: name of the user sending the message, message to send
	def send_message(self, sender, msg):
		for user in users:
			conns.send(sender, user.sock, msg)

	#adds the given user to the list of users
	#accepts: User object to add
	def add_user(self, user):
		if user not in users:
			users.append(user)
