import xmlrpc.client
server = xmlrpc.client.ServerProxy('http://localhost:9000')

multical = xmlrpc.client.MultiCall(server)
multical.ping()
multical.show_type(1)
multical.show_type('string')
for i, r in enumerate(multical()):
    print(i, r)