import threading
import time

def woker():
    print(threading.current_thread().getName(),'starting')
    time.sleep(0.2)
    print(threading.current_thread().getName(),'exiteing')

def my_service():
    print(threading.current_thread().getName(),'starting')
    time.sleep(0.3)
    print(threading.current_thread().getName(),'exitting')

t = threading.Thread(name='my_service',target=my_service)
w1 = threading.Thread(name='woker',target=woker)
w2 = threading.Thread(target=woker)

w1.start()
w2.start()
t.start()