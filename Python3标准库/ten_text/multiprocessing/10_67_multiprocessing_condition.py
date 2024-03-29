import multiprocessing
import time

def stager_1(cond):
    name = multiprocessing.current_process().name
    print('starting', name)
    with cond:
        print('{} done and ready for stagr 2'.format(name))
        cond.notify_all()

def stage_2(cond):
    name = multiprocessing.current_process().name
    print('starting',name)
    with cond:
        cond.wait()
        print('{} running'.format(name))

if __name__ == '__main__':
    condition = multiprocessing.Condition()
    s1 = multiprocessing.Process(
        name='s1',
        target=stager_1,
        args=(condition,)
    )

    s2_clients = [
        multiprocessing.Process(
            name='stage_2[{}]'.format(i),
            target=stage_2,
            args=(condition,)
        )
        for i in range(1,3)
    ]

    for c in s2_clients:
        c.start()
        time.sleep(1)
    s1.start()

    s1.join()
    for c in s2_clients:
        c.join()