import socket
import sys

def get_constants(prefix):
    return {
        getattr(socket, n):n
        for n in dir(socket)
        if n.startswith(prefix)
    }

families = get_constants('SOCK_')
types = get_constants('SOCK_')
protocols = get_constants('IPPROTO_')

sock = socket.create_connection(('localhost', 10000))

print('Family:',families[sock.family])
print('Type:',types[sock.type])
print('Protocol:',protocols[sock.proto])
print()

try:
    message = b'This is the message. It will be repeated.'
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
