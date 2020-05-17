import socket

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)

# Initialize all LEDs to off
GPIO.output(18, GPIO.LOW)
GPIO.output(23, GPIO.LOW)
GPIO.output(24, GPIO.LOW)
GPIO.output(25, GPIO.LOW)
GPIO.output(12, GPIO.LOW)

HOST = '0.0.0.0' # Server IP or Hostname
PORT = 12345 # Pick an open Port (1000+ recommended), must match the client sport
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
print('Socket created')

#managing error exception
try:
	s.bind((HOST, PORT))
except socket.error:
	print('Bind failed')

while True:
	s.listen(5)
	print('Socket awaiting messages')
	(conn, addr) = s.accept()
	print('Connected')

	# awaiting for message
	while True:
		data = conn.recv(1024)
		print('I sent a message back in response to: ' + data)
		reply = ''

		# process your message
		if data == 'on':
			GPIO.output(18, GPIO.HIGH)
			GPIO.output(23, GPIO.HIGH)
			GPIO.output(24, GPIO.HIGH)
			GPIO.output(25, GPIO.HIGH)
			GPIO.output(12, GPIO.HIGH)
			reply = 'led on'
		elif data == 'off':
			GPIO.output(18, GPIO.LOW)
			GPIO.output(23, GPIO.LOW)
			GPIO.output(24, GPIO.LOW)
			GPIO.output(25, GPIO.LOW)
			GPIO.output(12, GPIO.LOW)
			reply = 'led off'
		elif data == 'quit':
			conn.send('terminating')
			break
		else:
			reply = 'unknown command'

		# Sending reply
		conn.send(reply)
	conn.close() # Close connections
