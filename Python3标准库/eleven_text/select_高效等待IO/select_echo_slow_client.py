import socket
import sys
import time

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server_address = ('localhost', 10000)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)

time.sleep(1)

messages = [
    'Part one of the message.',
    'Part two of the message.',
]
amount_expected = len(''.join(messages))

try:
    for message in messages:
        data = message.encode()
        print('sending {}'.format(data),file=sys.stderr)
        sock.sendall(data)
        time.sleep(1.5)
        amount_received = 0
        while amount_received < amount_expected:
            data = sock.recv(16)
            amount_received += len(data)
            print('received {}'.format(data),file=sys.stderr)
finally:
    print('closing socket',file=sys.stderr)
    sock.close()