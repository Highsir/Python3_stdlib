from http import cookies

HTTP_COOKIE = '; '.join([
    r'integer=5',
    r'with_quotes="hello world"',
])

print('From constructor:')
c = cookies.SimpleCookie(HTTP_COOKIE)
print(c)

print()
print('From load:')
c = cookies.SimpleCookie()
c.load(HTTP_COOKIE)
print(c)