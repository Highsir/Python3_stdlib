import random
import threading
import time
import logging
"""
enumerate()会返回Thread实例的一个列表.这个列表也包括当前线程,由于等待当前线程终止(join)
会引入一种死锁情况,所以必须跳过.
"""

def worker():
    pause = random.randint(1,5) / 10
    logging.debug('sleeping %0.2f', pause)
    time.sleep(pause)
    logging.debug('ending')

logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s',
)

for i in range(3):
    t = threading.Thread(target=worker,daemon=True)
    t.start()

main_thread = threading.main_thread()
for t in threading.enumerate():
    if t is main_thread:
        continue
    logging.debug('joining %s', t.getName())
    t.join()