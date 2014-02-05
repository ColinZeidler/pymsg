import Room
import socket

class User:
	"""Class that defines a single client connection
	to the server. allows easier access to a clients 
	data, instead of using lots of maps"""
	rooms = []

	def __init__(self, conn, addr)
		self.sock = conn
		self.addr = addr	
		self.name = addr[0] #default the name of the client to their connecting ip

	#join a new room, will do nothing if user is already in the room
	#accepts Room object to join
	#returns True if succeeded, False if client already has the room
	def join_room(self, room):
		if room not in rooms:
			rooms.append(room)	#add the room to the clients list
			room.add_user(self)	#tell the room to add this client to its list
			print "user {} has added {} to thier list".format(self.name, room.name)
			return True
		return False

	#send a message to all rooms client is connected to
	#accepts: message to send
	def send_message(self, msg):
		for room in rooms:
			room.send_message(self.name, msg)
