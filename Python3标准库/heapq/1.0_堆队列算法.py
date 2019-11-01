from _heapq import heappush, heappop
from operator import lshift

# def heapsort(iterable):
#     h = []
#     for value in iterable:
#         heappush(h,value)
#     return [heappop(h) for i in range(len(h))]
# data = heapsort([1,3,5,7,9,2,4,6,8,0])
# print(data)
import itertools

pq = []
entry_finder = {}
REMOVED = '<removed-task>'
counter = itertools.count()

def add_task(task,priority=0):
    if task in entry_finder:
        remove_task(task)
    count = next(counter)
    entry = [priority, count, task]
    entry_finder[task] = entry
    heappush(pq,entry)

def remove_task(task):
    enrty = entry_finder.pop(task)
    enrty[-1] = REMOVED

def pop_task():
    while pq:
        priority, count, task = heappop(pq)
        if task is not REMOVED:
            del entry_finder[task]
            return task
    raise KeyError('pop form an empty prioriry queue')
for i in range(10):
    data = pop_task(i)
    print(data)