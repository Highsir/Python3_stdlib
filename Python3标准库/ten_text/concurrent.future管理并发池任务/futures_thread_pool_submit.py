from concurrent import futures
import threading
import time

def task(n):
    print('{}: sleeping {}'.format(threading.current_thread().name, n))
    time.sleep(0.1)
    print('{}: done with {}'.format(threading.current_thread().name,n))

    return n / 10

ex = futures.ThreadPoolExecutor(max_workers=2)
print('main: starting')
results = ex.submit(task, 5)
print('main: unprocessed results {}'.format(results))
print('main: waing for real results')
real_results = results.result()
print('main: results: {}'.format(real_results))