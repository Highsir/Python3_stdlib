import functools

def myfunc(a,b=2):
    print('called myfunc with:',(a,b))

def show_details(name,f,is_pattail=False):
    print('{}:'.format(name))
    print('object:',f)
    if not is_pattail:
        print('__name__:',f.__name__)
    if is_pattail:
        print('func:',f.func)
        print('args:',f.args)
        print('keyswords:',f.keywords)
    return

show_details('myfunc',myfunc)
myfunc('a',3)

p1 = functools.partial(myfunc,b=4)
show_details('pwnd',p1,True)
p1('passing a')
p1('override b',b=5)
print()

p2 = functools.partial(myfunc,'default a',b=99)
show_details('pwnd',p2,True)
p2()
p2(b='override b')
print()

print('insufficient arguments:')
p1()