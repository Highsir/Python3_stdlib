from http import cookies


c = cookies.SimpleCookie()
c['a'] = 5
c['b'] = 'hello world'

for name in ['a', 'b']:
    print(print(c[name].key))
    print(' {}'.format(c[name]))
    print(' value={}'.format(c[name].value))
    print(' coded_value={}'.format(c[name].coded_value))
    print()