import threading
import time
import logging

def worker():
    logging.debug('starting')
    time.sleep(0.2)
    logging.debug('exiting')

def my_service():
    logging.debug('starting')
    time.sleep(0.3)
    logging.debug('exiting')

logging.basicConfig(
    level=logging.DEBUG,
    format='[%(levelname)s] (%(threadName)-10s) %(message)s',
)

t = threading.Thread(name='my_service', target=my_service)
w1 = threading.Thread(name='worker', target=worker)
w2 = threading.Thread(target=worker)

w1.start()
w2.start()
t.start()