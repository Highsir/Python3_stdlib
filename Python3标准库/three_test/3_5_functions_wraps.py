import functools

def show_details(name,f):
    print('{}:'.format(name))
    print(' object:',f)
    print('__name__:', end='')
    try:
        print(f,__name__)
    except AttributeError:
        print('(no __name__)')
    print(' __doc__:', repr(f.__doc__))
    print()

def simple_decorator(f):
    @functools.wraps(f)
    def decorator(a='decorator defaults', b=1):
        print(' decoratored:',(a, b))
        print(' ',end='')
        return f(a, b=b)
    return decorator

def myfunc(a, b=2):
    print(' myfunc:', (a, b))
    return

show_details('myfunc', myfunc)
myfunc('unwrapped, default b')
myfunc('unwrapped, passing b',3)
print()

wrapped_myfunc = simple_decorator(myfunc)
show_details('wrapped_myfunc', wrapped_myfunc)
wrapped_myfunc()
wrapped_myfunc('args to wrapped', 4)
print()

@simple_decorator
def decorated_myfunc(a, b):
    myfunc(a, b)
    return

show_details('decorated_myfunc', decorated_myfunc)
decorated_myfunc()
decorated_myfunc('args to decorated', 4)