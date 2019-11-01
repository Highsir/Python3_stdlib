import socket
import sys
import os

server_address = './uds_socket'

try:
    os.unlink(server_address)
except OSError:
    if os.path.exists(server_address):
        raise

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

print('start up on {}'.format(server_address))
sock.bind(server_address)
sock.listen(1)

while True:
    print('wait for a connection')
    connection, client_address = sock.accept()
    try:
        print('connection from',client_address)
        while True:
            data = connection.recv(16)
            print('received {}'.format(data))
            if data:
                print('sending data back to the client')
                connection.sendall(data)
            else:
                print('no data from',client_address)
                break
    finally:
        connection.close()