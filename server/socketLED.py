import socket

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)

HOST = '0.0.0.0' # Server IP or Hostname
PORT = 12345 # Pick an open Port (1000+ recommended), must match the client sport
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
print 'Socket created'

#managing error exception
try:
	s.bind((HOST, PORT))
except socket.error:
	print 'Bind failed '

s.listen(5)
print 'Socket awaiting messages'
(conn, addr) = s.accept()
print 'Connected'

# awaiting for message
while True:
	data = conn.recv(1024)
	print 'I sent a message back in response to: ' + data
	reply = ''

	# process your message
	if data == 'on':
		GPIO.output(18, GPIO.HIGH)
		reply = "led on"
	elif data == 'off':
		GPIO.output(18, GPIO.LOW)
		reply = "led off"
	elif data == 'quit':
		conn.send('terminating')
		break
	else:
		reply = 'unknown command'

	# Sending reply
	conn.send(reply)
conn.close() # Close connections
