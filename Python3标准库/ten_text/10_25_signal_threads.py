import signal
import threading
import os
import time
"""信号处理器都在主线程中注册,因为这是Python的signal模块实现的一个要求,不论底层平台如何支持
线程和信号的结合,都有这个要求.尽管接红藕线程调用了signal.pause(),但它不会接收信号.这个列子快要结束时
的signal.alarm(2)调用避免了无线阻塞,因为接收者线程永远不会退出.
"""

def signal_handler(num,stack):
    print('receved signal {} in {}'.format(num,threading.currentThread().name))

signal.signal(signal.SIGUSR1,signal_handler)

def wait_for_signal():
    print('waiting for signal in' , threading.currentThread().name)
    signal.pause()
    print('done waiting')

receiver = threading.Thread(target=wait_for_signal,name='receiver')
receiver.start()
time.sleep(0.1)

def send_signal():
    print('sending signal in',threading.currentThread().name)
    os.kill(os.getpid(),signal.SIGUSR1)

sender = threading.Thread(target=send_signal,name='sender')
sender.start()
sender.join()

print('waiting for', receiver.name)
signal.alarm(2)
receiver.join()