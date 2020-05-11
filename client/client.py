import socket

HOST = '10.0.1.87' # Enter IP or Hostname of your server
PORT = 12345 # Pick an open Port (1000+ recommended), must match the server port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))

#Lets loop awaiting for your input
while True:
    command = input('Enter your command: ')
    # command = 'Sent Command'
    s.sendall(command.encode('utf-8'))
    reply = s.recv(1024)
    rep = reply.decode('utf-8')
    if rep == 'Terminating':
    	break
    print(rep)