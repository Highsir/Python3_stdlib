from http import cookies

c = cookies.SimpleCookie()
c['mycookies'] = 'cookies_value'
print(c)