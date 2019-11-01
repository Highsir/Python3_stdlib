import logging
import random
import threading
import time
"""
控制资源访问:
除了同步线程操作,还有一点很重要,要能够控制对共享资源的访问,从而避免破坏或丢失数据.
Python的内置数据结构(列表,字典等)是线程安全的,这是Python使用原子字节码来管理这些
数据结构的一个副作用(更新过程中不会释放保护Python内部数据结构的全局解释器锁GIL).
Python中实现的其他数据结构或更简单的类型(如整数和浮点数)则没有这个保护.要保证同时
安全的访问一个对象,可以用一个Lock对象.
"""

class Counter:

    def __init__(self,start=0):
        self.lock = threading.Lock()
        self.value = start

    def increment(self):
        logging.debug('waiting for lock')
        self.lock.acquire()
        try:
            logging.debug('Acquired lock')
            self.value = self.value + 1
        finally:
            self.lock.release()

def worker(c):
    for i in range(2):
        pause = random.random()
        logging.debug('Sleeping %0.02f', pause)
        time.sleep(pause)
        c.increment()
    logging.debug('Done')

logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s',
)
counter = Counter()
for i in range(2):
    t = threading.Thread(target=worker,args=(counter,))
    t.start()


logging.debug('Waiting for worker threads')
main_thread = threading.main_thread()

for t in threading.enumerate():
    if t is not main_thread:
        t.join()
logging.debug('Counter: %d', counter.value)