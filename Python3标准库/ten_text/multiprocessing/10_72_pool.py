import multiprocessing

def do_calculation(data):
    return data * 2

def start_process():
    print('start',multiprocessing.current_process().name)

if __name__ == '__main__':
    inputs = list(range(10))
    print('Inout  :',inputs)

    builtin_outputs = list(map(do_calculation,inputs))
    print('built-in',builtin_outputs)

    pool_size = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(
        processes=pool_size,
        initializer=start_process,
        # 告诉进程池在完成一些任务之后要重新启动一个工作进程,
        # 来避免长时间运行的工作进程消耗更多的资源
        maxtasksperchild=2,
    )
    pool_outputs = pool.map(do_calculation,inputs)
    pool.close()
    pool.join()

    print('Pool:',pool_outputs)