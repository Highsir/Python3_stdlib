from xmlrpc.server import SimpleXMLRPCServer
import os
import inspect

server = SimpleXMLRPCServer(('localhost',9000),logRequests=True)

def expose(f):
    f.exposed = True
    return f

def is_exposed(f):
    return getattr(f, 'exposed', False)

class Myservice:
    PREFIX = 'prefix'

    def _dispatch(self, method, params):
        if not method.startswith(self.PREFIX + '.'):
            raise Exception(
                'method "{}" is not supported'.format(method)
            )
        method_name = method.partition('.')[2]
        func = getattr(self, method_name)
        if not is_exposed(func):
            raise Exception(
                'method "{}" is not supported'.format(method)
            )
        return func(*params)
    @expose
    def public(self):
        return 'This is public'

    def private(self):
        return 'This is private'

server.register_instance(Myservice())

try:
    server.serve_forever()
except KeyboardInterrupt:
    print('EXiting')