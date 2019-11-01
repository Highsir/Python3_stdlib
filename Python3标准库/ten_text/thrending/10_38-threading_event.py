import logging
import threading
import time
"""
线程间传送信号:
尽管使用多线程的目的是并发地运行单独的操作,但有时也需要在两个或者多个线程中同步操作.
事件对象是实现线程间安全通信的一种简单方法.Event管理一个内部标志,调用者可以用set()和
clear()方法控制这个标志.其他线程可以使用wait()暂停,直到这个标志被设置,可有效地阻塞
进程直至允许这些线程继续.
wait()方法取一个参数,表示等待事件的时间(秒数),达到这个时间后就超时.它会返回一个布尔值,
指示事件是否已设置,使调用者知道wait()为什么返回.可以对事件单独地使用is_set()方法而
不必担心阻塞.
"""

def wait_for_event(e):
    logging.debug('wait_for_event starting')
    event_is_set = e.wait()
    logging.debug('event set: %s',event_is_set)

def wait_for_event_timeout(e,t):
    while not e.is_set():
        logging.debug('wait_for_event_timeout starting')
        event_is_set = e.wait(t)
        logging.debug('event set: %s',event_is_set)
        if event_is_set:
            logging.debug('processing event')
        else:
            logging.debug('doing other work')

logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s',
)

e = threading.Event()
t1 = threading.Thread(
    name='block',
    target=wait_for_event,
    args=(e,)
)
t1.start()

t2 = threading.Thread(
    name='nonblock',
    target=wait_for_event_timeout,
    args=(e,2),
)
t2.start()

logging.debug('Waiting before calling Event.set()')
time.sleep(0.3)
e.set()
logging.debug('Event is set')