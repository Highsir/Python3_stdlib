import select
import socket
import sys
import queue

# create a TCP/IP socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(0)

server_address = ('localhost',10000)
print('starting up on {} port {}'.format(*server_address))
server.bind(server_address)

server.listen(5)

# sockets from which we expect to read
inputs = [server]

# sockets to which we expect to write
outputs = []

# outgoing message queue
message_queue = {}

while inputs:
    print('waiting for the next event', file=sys.stderr)
    readable,writeable, exceptional = select.select(inputs, outputs, inputs)

    # handle inputs
    for s in readable:
        if s is server:
            connection, client_address = s.accept()
            print('connection from ', client_address,file=sys.stderr)
            connection.setblocking(0)
            inputs.append(connection)

            message_queue[connection] = queue.Queue()
        else:
            data = s.recv(1024)
            if data:
                print('received {} from {}'.format(data, s.getpeername()), file=sys.stderr)
                message_queue[s].put(data)
                # add output channel for response
                if s not in outputs:
                    outputs.append(s)
            else:
                print('clsing', client_address, file=sys.stderr)
                if s in outputs:
                    outputs.remove(s)
                inputs.remove(s)
                s.close()

                # remove message queue
                del message_queue[s]

    # handle outputs
    for s in writeable:
        try:
            next_msg = message_queue[s].get_nowait()
        except queue.Empty:
            print(' ',s.getpeername(), 'queue empty', file=sys.stderr)
            outputs.remove(s)
        else:
            print('sending {} to {}'.format(next_msg,s.getpeername()),file=sys.stderr)
            s.send(next_msg)

    # handle "exceptional conditions"
    for s in exceptional:
        print('exception condition on', s.getpeername(),file=sys.stderr)
        # stop listiening for input on the connection
        inputs.remove(s)
        if s in outputs:
            s.closse()
        del message_queue[s]
