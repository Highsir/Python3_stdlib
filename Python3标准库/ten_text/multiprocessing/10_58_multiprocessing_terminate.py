import multiprocessing
import time


def show_worker():
    print('start worker')
    time.sleep(0.1)
    print('finished worker')


if __name__ == '__main__':
    p = multiprocessing.Process(
        target=show_worker
    )

    print('before:',p,p.is_alive())

    p.start()
    print('during:',p,p.is_alive())

    p.terminate()
    print('terminated:',p,p.is_alive())

    p.join()
    print('joined:',p,p.is_alive())