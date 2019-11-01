from collections import Iterator,Iterable

import functools
@functools.lru_cache()
def expnesive(a,b):
    print('expesive({},{})'.format(a,b))
    return a * b


MAX = 2
for i in range(MAX):
    for j in range(MAX):
        expnesive(i,j)
print(expnesive.cache_info())

arr = [1,2,3]
print(isinstance(arr,Iterator))
print(isinstance(arr,Iterable))