import socket
import struct
import sys

message = b'very important data'
multicast_group = ('224.3.29.71', 10000)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(0.2)

ttl = struct.pack('b', 1)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

try:
    print('sending {}'.format(message))
    sent = sock.sendto(message, multicast_group)
    while True:
        print('waiting to receive')
        try:
            data, server = sock.recvfrom(16)
        except socket.timeout:
            print('timed out, no more response')
            break
        else:
            print('received {} from {}'.format(data, server))
finally:
    print('closing socket')
    sock.close()