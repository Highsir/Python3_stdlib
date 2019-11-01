from functools import wraps
def my_decorator(f):
    @wraps(f)
    def wrapper(*args,**kwds):
        print('calling decorated function')
        return f(*args,**kwds)
    return wrapper

@my_decorator
def example():
    print('calling example function')

example()