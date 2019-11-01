import ipaddress

ADDRESSES = [
    '10.9.0.6',
    'fdfd:87b5:b475:5e3e:b1bc:e121:a8eb:14aa',
]

for n in ADDRESSES:
    net = ipaddress.ip_address(n)
    print('{}'.format(net))
    for i, ip in zip(range(3), net.hosts()):
        print(ip)
    print()