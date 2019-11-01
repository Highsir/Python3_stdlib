import os
import socketserver
import threading

class ThreadedEchoRequestHandler(socketserver.BaseRequestHandler):

    def handle(self):
        data = self.request.recv(1024)
        cur_pid = os.getpid()
        response = b'%d: %s' % (cur_pid, data)
        self.request.send(response)
        return

class ForkingEchoServer(socketserver.ForkingMixIn,socketserver.TCPServer):
    pass

if __name__ == '__main__':
    import socket

    address = ('localhost', 0)
    server =ForkingEchoServer(address, ThreadedEchoRequestHandler)

    ip ,port = server.server_address

    t = threading.Thread(target=server.serve_forever)
    t.setDaemon(True)
    t.start()
    print('Server loop running in process:', os.getpid())

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))

    message = b'Hello world'
    print('Sending : {}'.format(message))
    len_sent = s.send(message)

    response = s.recv(1024)
    print('Received : {}'.format(response))

    server.shutdown()
    s.close()
    server.socket.close()