import xmlrpc.client

server = xmlrpc.client.ServerProxy('http://localhosy:9000')

try:
    server.raise_exception('A message')
except Exception as err:
    print('Fault code:',err.faultCode)
    print('Message  :',err.faultString)