import conns
import socket

commands = 	{'/dc':2,   #disconnect client from server,	/dc {reason/msg}
			'/stop':2,  #tell server to stop running,		/stop {passwd}
			'/join':2,  #join given channel,				/join {channel}
			'/leave':2, #leave given channel,				/leave {channel}
			'/to':3}    #send to given channel, 			/to {channel} {msg}
hasMsg = ['/dc', '/to']

def parse_msg(msg, con):
	strings = msg.split(" ")
	cmd = strings[0]
	if cmd in commands:
		if cmd == "/dc":
			server_dc(" ".join(strings[commands.get(cmd):]), con)
		elif cmd == "/stop":
			pass
		elif cmd == "/join":
			pass
		elif cmd == "/leave":
			pass
		elif cmd == "/to":
			pass
	else: #msg does not contain a command
		for person in conns.clients.keys():
			if person == con:
				continue
			conns.send(conns.clients.get(con)[0], person, msg)

def server_dc(msg, con):
	print "disconnecting client"
	for person in conns.clients.keys():
		conns.send(conns.SERVER_STR, person, conns.clients.get(con)[0] + " Disconnected")
	con.close()
	del conns.clients[con]

def client_dc(msg):
	pass

def stop(passwd):
	pass

def join(room):
	pass

def leave(room):
	pass

def to(room, msg):
	pass
