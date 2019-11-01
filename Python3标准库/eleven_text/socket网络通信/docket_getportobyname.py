import socket

"""
获取分配给一个传输协议的端口号;
协议码是标准化的,在socket中被定义为常量,这些协议码都有前缀IPPORTO_.
"""
def get_constants(prefix):
    return {
        getattr(socket, n):n
        for n in dir(socket)
        if n.startswith(prefix)
    }

protocols = get_constants('IPPROTO_')
print(protocols)
print()

for name in ['icmp', 'udp', 'tcp']:
    proto_num = socket.getprotobyname(name)
    const_name = protocols[proto_num]
    print('{} -> {} (socket.{} = {})'.format(
        name, proto_num, const_name,
        getattr(socket, const_name)))