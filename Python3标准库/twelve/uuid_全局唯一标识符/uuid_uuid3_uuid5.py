import uuid

hostname = ['www.doughellmann.com', 'blog.doughellmann.com']

for name in hostname:
    print(name)
    print('MD5      :',uuid.uuid3(uuid.NAMESPACE_DNS,name))
    print('SHA_1    :',uuid.uuid5(uuid.NAMESPACE_DNS,name))
    print()