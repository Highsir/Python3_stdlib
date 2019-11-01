import socket
import os

parent, child = socket.socketpair()
pid = os.fork()

if pid:
    print('in parent, sending message')
    child.close()
    parent.sendall(b'ping')
    response = parent.recv(1024)
    print('response from child:',response)
    parent.close()

else:
    print('in child, waaiting for message')
    parent.close()
    message = child.recv(10224)
    print('message from parent:',message)
    child.sendall(b'pong')
    child.close()