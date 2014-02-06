#handling all of the connection methods
import socket
from Room import Room

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = ''
PORT = 60000

FLAG = False
SERVER_STR = "Server"
PASS = "goaway"

clients	= {}
rooms 	= {"root" : Room("root")}
#nicks   = {}

def send(sender, receiver, msg):
	receiver.send(sender + ": " + msg)
