import logging
import threading
import random
import time

# 限制资源的并发访问
"""
有事可能需要允许多个线程同时访问一个资源,但要限制总数.例如,连接池支持同时连接
"""

class ActivePool:
    def __init__(self):
        super(ActivePool,self).__init__()
        self.active = []
        self.lock = threading.Lock()

    def makeActive(self,name):
        with self.lock:
            self.active.append(name)
            logging.debug('Running: %s', self.active)

    def makeInactive(self,name):
        with self.lock:
            self.active.remove(name)
            logging.debug('Running: %s', self.active)


def wooker(s,pool):
    logging.debug('Waiting to join the pool')
    with s:
        name = threading.current_thread().getName()
        var = pool.makeActive(name)
        time.sleep(0.1)
        pool.makeInactive(name)

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s (%(threadName)-2s) %(message)s',
)

pool = ActivePool()
s = threading.Semaphore(3)
for i in range(4):
    t = threading.Thread(
        target=wooker,
        name=str(i),
        args=(s,pool)

    )
    t.start()