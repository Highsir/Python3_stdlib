import select
import socket
import sys
import queue

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(0)

server_address = ('localhost', 10000)
print('starting up on {} port {}'.format(*server_address), file=sys.stderr)
server.bind(server_address)

server.listen(5)

message_queue = {}

TIME_OUT = 1000

READ_ONLY = (
    select.POLLIN |
    select.POLLPRI |
    select.POLLHUP |
    select.POLLERR
)
READ_WRITE = READ_ONLY | select.POLLOUT

# set up the poller

poller = select.poll()
poller.register(server, READ_ONLY)

# Map file descriptors to socket object
fd_to_socket = {
    server.fileno(): server
}
while True:
    # print('waiting for the next event',file=sys.stderr)
    events = poller.poll(TIME_OUT)
    for fd, flag in events:
        s = fd_to_socket[fd]
        if flag & (select.POLLIN | select.POLLPRI):
            if s is server:
                connection, client_address = s.accept()
                print('  connection',client_address,file=sys.stderr)
                connection.setblocking(0)
                fd_to_socket[connection.fileno()] = connection
                poller.register(connection, READ_ONLY)

                # give the connection a queue for data to send
                message_queue[connection] = queue.Queue()
            else:
                data = s.recv(1024)

                if data:
                    # A readable client socket has data
                    print('  received {} from {}'.format(data, s.getpeername()),file=sys.stderr)
                    message_queue[s].put(data)
                    poller.modify(s, READ_WRITE)
                else:
                    # Interpret empty result as closed connection
                    print('  closing', client_address,file=sys.stderr)
                    # stop listening for input on the connection
                    poller.unregister(s)
                    s.close()
                    del message_queue[s]
        elif flag & select.POLLHUP:
            # Client hung up
            print('  closing', client_address,'(HUP)', file=sys.stderr)
            poller.unregister(s)
            s.close()

        elif flag & select.POLLOUT:
            # socket is ready to send data
            try:
                next_msg = message_queue[s].get_nowait()
            except queue.Empty:
                # no messages waiting, so stop checking
                print(s.getpeername(), 'queue empty',file=sys.stderr)
                poller.modify(s, READ_ONLY)
            else:
                print('  sending {} to {}'.format(next_msg, s.getpeername()),file=sys.stderr)
                s.send(next_msg)
        elif flag & select.POLLERR:
            print('exception on', s.getpeername(), file=sys.stderr)
            poller.unregister(s)
            s.close()
            del message_queue[s]