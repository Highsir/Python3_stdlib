import threading
import time
import logging

'''
守护线程.这个线程可以一直运行而不阻塞主程序退出.如果一个服务不能很容易的中断线程,
或者即使让线程工作到一半时终止也不会造成数据损失或破坏,那么对于这些服务,使用守护线程就很有用.
要标志一个线程为守护线程,构造线程时便要传入daemon=True或调用它的setDaemon()方法并提供参数
True.默认情况下线程不作为守护线程.
下面这个代码的输出不包含守护线程的'exiting'消息,因为在从sleep()调用唤醒守护线程之前,
所有非守护线程(包括主线程)已经退出.要等待一个守护线程完成工作,需要用join()方法.
默认的,join()会无限阻塞.或者还可以传入一个浮点值,表示等待线程在多长时间后变为不活动.
即使线程在这个时间段内未完成,join()也会返回.
'''

def daemon():
    logging.debug('starting')
    time.sleep(0.2)
    logging.debug('exiting')

def non_daemon():
    logging.debug('starting')
    # time.sleep(2)
    logging.debug('exiting')

logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s',
)

d = threading.Thread(name='daemon', target=daemon,daemon=True)
t = threading.Thread(name='non_daemon', target=non_daemon)

d.start()
t.start()

d.join(0.1)
# 由于传入的超时时间小于守护线程睡眠的时间,所以join()返回之后这个线程仍然'活着'
print('d.isAlive()',d.isAlive())
t.join()