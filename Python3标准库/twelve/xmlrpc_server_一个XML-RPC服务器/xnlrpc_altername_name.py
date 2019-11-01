from xmlrpc.server import SimpleXMLRPCServer
import os

server = SimpleXMLRPCServer(('localhost',9000))

def list_contents(dir_name):
    return os.listdir(dir_name)

server.register_function(list_contents,'dir')

try:
    server.serve_forever()
except KeyboardInterrupt:
    print('Exiting')