import ipaddress

"""
网络实例是可迭代的,会提供网络上的地址
"""

NETWORKS = [
    '127.0.0.1/24',
    'fdfd:87b5:b475:5e3e::/64',
]
for n in NETWORKS:
    net = ipaddress.ip_address(n)
    print('{}'.format(net))
    for i ,ip in zip(range(3), net):
        print(ip)
    print()