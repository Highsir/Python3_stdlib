import socket

for host in ['apu', 'www.pymotw.com']:
    print('{} : {}'.format(host, socket.getfqdn(host)))