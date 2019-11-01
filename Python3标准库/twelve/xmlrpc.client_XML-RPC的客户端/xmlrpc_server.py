"""
XML-RPC是一个轻量级远程过程调用协议,建立在HTTP和XML之上.xmlrpclib模块
允许Python程序与任何语言编写的XML-RPC服务器通信.
"""
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.client import Binary
import datetime

class ExampleService:
    def ping(self):

        return True

    def now(self):

        return datetime.datetime.now()

    def show_type(self,arg):

        return (str(arg), str(type(arg)), arg)

    def raise_exception(self, msg):

        raise RuntimeError(msg)

    def send_back_binary(self,bin):
        data = bin.data
        print('send_back_binary({})'.format(data))
        response = Binary(data)
        return response

if __name__ == '__main__':
    server = SimpleXMLRPCServer(('localhost', 9000),
                                logRequests=True,
                                allow_none=True)
    server.register_introspection_functions()
    server.register_function()
    server.register_instance(ExampleService())

    try:
        print('Use Control-C to exit.')
        server.serve_forever()
    except KeyboardInterrupt :
        print('EXiting')