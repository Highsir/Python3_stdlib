import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 10000)
print('connection to {} port {}'.format(*server_address))
sock.connect(server_address)

try:
    message = b'This is the message, It will be repeated.'
    print('sending {}'.format(message))
    sock.sendall(message)

    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print('received {}'.format(data))

finally:
    print('closing socket')
    sock.close()