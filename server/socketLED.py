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
	if data == 'Hello':
		reply = 'Hi, back!'
	elif data == 'This is important':
		reply = 'OK, I have done the important thing you have asked me!'
<<<<<<< HEAD
    elif data == 'Light':
        print ("LED On")
        GPIO.output(18, GPIO.HIGH)
        time.sleep(5)
        print ("LED off")
        GPIO.output(18, GPIO.LOW)
        reply = "LED done"
=======
    	elif data == 'Light':
        	print ("LED On")
        	GPIO.output(18, GPIO.HIGH)
        	time.sleep(5)
        	print ("LED off")
        	GPIO.output(18, GPIO.LOW)
>>>>>>> dcd988eefe0a29d0435a30c581292d84cfecd886

	#and so on and on until...
	elif data == 'quit':
		conn.send('Terminating')
		break
	else:
		reply = 'Unknown command'

	# Sending reply
	conn.send(reply)
conn.close() # Close connections
