import logging
import threading
import time

"""
除了使用Event,还可以通过使用一个Condition对象来同步线程.由于Condition使用了一个Lock,
所以它可以绑定到一个共享资源,允许多个线程等待资源更新.在这个例子中,consumer()线程要等待
设置了Condition才能继续.producer(0线程负责设置条件,以及通知其他线程继续.
"""
def consumer(cond):
    logging.debug('Starting consumer thread')
    with cond:
        cond.wait()
        logging.debug('Resource is available to consumer')

def producer(cond):
    logging.debug('Starting producer thread')
    with cond:
        logging.debug('Making resource available')
        cond.notifyAll() # 通知其它线程继续


logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s (%(threadName) -2s) %(message)s',
)

condition = threading.Condition()
c1 = threading.Thread(name='c1',target=consumer,args=(condition,))
c2 = threading.Thread(name='c2',target=producer,args=(condition,))

p = threading.Thread(name='p',target=producer,args=(condition,))

c1.start()
time.sleep(0.2)
c2.start()
time.sleep(0.2)
p.start()