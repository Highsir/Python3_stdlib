import threading
import time

"""
屏障(barrier)另一种线程同步机制.Barrier会建立一个控制点,所有参与线程会在这里阻塞,直到所有
这些参与'方'都达到这一点.采用这种方法,线程可以单独启动然后暂停,直到所有线程都准备好才可以继续.
在这个例子中,Barrier被配置为会阻塞线程,直到3个线程都在等待.满足这个条件时,所有线程被同时释放
从而越过这个控制点.wait()的返回值指示了释放的参与线程数,可以用来限制一些线程做清理资源等动作.
"""
def worker(barrier):
    print(threading.current_thread().name,
          'waiting for barrier with {} others'.format(barrier.n_waiting))
    worker_id = barrier.wait()
    print(threading.current_thread().name,'after barrier',worker_id)

NUM_THREADS = 3

barrier = threading.Barrier(NUM_THREADS)

threads = [
    threading.Thread(
        target=worker,
        args=(barrier,)
    )
    for i in range(NUM_THREADS)
]
for t in threads:
    print(t.name,'starting')
    t.start()
    time.sleep(1)

for t in threads:
    t.join()