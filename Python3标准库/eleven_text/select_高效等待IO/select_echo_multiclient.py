import socket
import sys

messages = [
    'This is the message. ',
    'It will be sent. ',
    'in parts.'
]
server_address = ('localhost', 10000)

# create TCP/IP socket
socks = [
    socket.socket(socket.AF_INET,socket.SOCK_STREAM),
    socket.socket(socket.AF_INET,socket.SOCK_STREAM),
]

print('connecting to {} port {}'.format(*server_address),file=sys.stderr)

for s in socks:
    s.connect(server_address)

for message in messages:
    outgoing_data = message.encode()
    for s in socks:
        print('{}: sending {}'.format(s.getpeername(),outgoing_data),file=sys.stderr)
        s.send(outgoing_data)
    for s in socks:
        data = s.recv(1024)
        print('{}:received {}'.format(s.getpeername(),data),file=sys.stderr)
        if not data:
            print('closing socket',s.getpeername(),file=sys.stderr)
            s.close()