import threading
import logging

def worekr_with(lock):
    with lock:
        logging.debug('Lock acquired via with')

def worker_no_with(lock):
    lock.acquire()
    try:
        logging.debug('Lock acquire direcyly')
    finally:
        lock.release()

logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s',
)

lock = threading.Lock()
w = threading.Thread(target=worekr_with,args=(lock,))
nw = threading.Thread(target=worker_no_with,args=(lock,))

w.start()
nw.start()