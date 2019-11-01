import socket

hostname, aliases, addresses = socket.gethostbyaddr('66.33.211.242')
print('Hostname :', hostname)
print('Aliases:', aliases)
print('Addresses: ',addresses)