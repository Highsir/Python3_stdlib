import binascii
import socket
import struct
import sys

for string_address in ['192.168.1.1', '127.0.0.1']:
    packed= socket.inet_aton(string_address)
    print('Original:',string_address)
    print('Packed:', binascii.hexlify(packed))
    print('Unpacked:', socket.inet_ntoa(packed))
    print()


# ipv6
print('ipv6')
string_addr = '2002:ac10:10a:1234:21e:52ff:fe74:40e'
packed= socket.inet_pton(socket.AF_INET6, string_addr)
print('Original:',string_addr)
print('Packed:', binascii.hexlify(packed))
print('Unpacked:', socket.inet_ntop(socket.AF_INET6, packed))
print()