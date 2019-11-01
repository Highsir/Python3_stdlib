import socket

"""
getaddrinfo()将一个服务的基本地址转换为一个元组列表,其中包含建立一个链接所需的全部信息.
每个元组可能包含不同的网络族或协议
"""

def get_constants(prefix):
    return {
        getattr(socket, n): n
        for n in dir(socket)
        if n.startswith(prefix)
    }

families = get_constants('AF_')
types = get_constants('SOCK_')
protocols = get_constants('IPPROTO_')

for response in socket.getaddrinfo('www.python.org', 'http'):
    family, socktype, proto, canonname, sockaddr = response
    print('Family:',families[family])
    print('Type:',types[socktype])
    print('protocol:',protocols[proto])
    print('Canonical name:',canonname)
    print('Socket address:', sockaddr)
    print()