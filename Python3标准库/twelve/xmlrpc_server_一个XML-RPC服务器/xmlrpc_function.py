from xmlrpc.server import SimpleXMLRPCServer
import logging
import os

# set up logging
logging.basicConfig(level=logging.INFO)
server = SimpleXMLRPCServer(('localhost',9000),logRequests=True)

# Expose a function
def list_contents(dir_name):
    logging.info('list_contents(%s)', dir_name)
    return os.listdir(dir_name)

server.register_function(list_contents)

# 开启服务器
try:
    print('Use Control-C to exit')
    server.serve_forever()
except KeyboardInterrupt:
    print('Exiting')
