import signal
import threading
import os
import time

def signal_handler(num,stack):
    print(time.ctime(),'alarm in', threading.currentThread().name)

signal.signal(signal.SIGALRM,signal_handler)

def use_alarm():
    t_name = threading.currentThread().name
    print(time.ctime(),'setting alarm in',t_name)
    signal.alarm(1)
    print(time.ctime(),'sleeping in', t_name)
    time.sleep(5)
    print(time.ctime(),'done with sleep in', t_name)

alarm_threaad = threading.Thread(target=use_alarm,name='alarm_thread')

alarm_threaad.start()
time.sleep(0.1)

print(time.ctime(),'waiting for',alarm_threaad.name)
alarm_threaad.join()

print(time.ctime(),'exiting normally')