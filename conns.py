#handling all of the connection methods
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = ''
PORT = 60000

FLAG = False
SERVER_STR = "Server"
PASS = "goaway"

clients = {}
nicks   = {}

def send(sender, receiver, msg):
	receiver.send(sender + ": " + msg)
