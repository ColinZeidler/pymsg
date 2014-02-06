import conns
import socket, sys
from Room import Room

commands = 	{'/dc':1,   #disconnect client from server,	/dc {reason/msg}
			'/stop':1,  #tell server to stop running,		/stop {passwd}
			'/join':1,  #join given channel,				/join {channel}
			'/leave':1, #leave given channel,				/leave {channel}
			'/to':2,    #send to given channel, 			/to {channel} {msg}
			'/setnick':1}

hasMsg = ['/dc', '/to']

def parse_msg(msg, con):
	strings = msg.split(" ")
	cmd = strings[0]
	if cmd in commands:
		if cmd == "/dc":
			server_dc(" ".join(strings[commands.get(cmd):]), con)
		elif cmd == "/stop":
			stop(strings[1])
		elif cmd == "/join": #the user is joining a room
			join(strings[1], con)
		elif cmd == "/leave": #the user is leaving a room
			leave(strings[1], con)
		elif cmd == "/setnick": #the user is changing their screen name
			set_nick(strings[1], con)
		elif cmd == "/to":
			pass
	else: #msg does not contain a command
		conns.clients.get(con).send_message(msg)

def server_dc(msg, con):
	print "disconnecting client"
	broadcast_all(conns.SERVER_STR, conns.clients.get(con).name + " Disconnected")
	con.close()
	del conns.clients[con]

def stop(passwd):
	if passwd == conns.PASS:
		broadcast_all("/dc ", "")
		conns.FLAG = True

def join(room, con):
	user = conns.clients.get(con)
	if room in conns.rooms:
		chan = conns.rooms.get(room)
	else:
		chan = Room(room)
		conns.rooms[room] = chan
	user.join_room(chan)
	pass

def leave(room, con):
	user = conns.clients.get(con)
	if room in conns.rooms:
		chan = conns.rooms.get(room)
	else:
		return
	user.leave_room(chan)

def to(room, msg):
	pass

def set_nick(name, con):
	prevName = conns.clients.get(con).name
	conns.clients.get(con).name = name
	print "set nickname to:", name
	broadcast_all(conns.SERVER_STR, prevName + " changed name to " + name) 


def broadcast_all(sender, msg):
	for person in conns.clients.keys():
		conns.send(sender, person, msg)
