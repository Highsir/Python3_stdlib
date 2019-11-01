import functools
import inspect
from pprint import pprint

@functools.total_ordering
class MyObject():
    def __init__(self,val):
        self.val = val

    def __eq__(self, other):
        print('testing __eq__({},{})'.format(self.val,other.val))
        return self.val == other.val

    def __gt__(self, other):
        print('testing __eq__({},{})'.format(self.val, other.val))
        return self.val == other.val

print('Methods:\n')
pprint(inspect.getmembers(MyObject,inspect.isfunction))

a = MyObject(1)
b = MyObject(2)

print('\nComparisons:')
for i in ['a<b','a<=b','a==b','a>=b','a>b']:
    print('\n{:6}:'.format(i))
    result = eval(i)
    print('result of {}:{}'.format(i,result))