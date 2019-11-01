import multiprocessing
import time

class Consumer(multiprocessing.Process):

    def __init__(self,task_queue,result_queue):
        multiprocessing.Process.__init__(self)
        self.task_queue = task_queue
        self.result_queue = result_queue

    def run(self):
        proc_name = self.name

        while True:
            next_task = self.task_queue.get()
            if next_task is None:
                print('{}:Exiting'.format(proc_name))
                self.task_queue.task_done()
                break
            print('{}:{}'.format(proc_name,next_task))
            answer = next_task()
            self.task_queue.task_done()
            self.result_queue.put(answer)

class Task:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def __call__(self, *args, **kwargs):
        time.sleep(0.1)
        return '{self.a} * {self.b} = {product}'.format(
            self=self,product = self.a * self.b
        )

    def __str__(self):
        return '{self.a} * {self.b}'.format(self=self)


if __name__ == '__main__':
    # 建立通信队列
    tasks = multiprocessing.JoinableQueue()
    results = multiprocessing.Queue()

    # 开始consumer
    num_consumers = multiprocessing.cpu_count() * 2
    print('creating {} consumer'.format(num_consumers))
    consumers = [
        Consumer(tasks,results)
        for i in range(num_consumers)
    ]
    for w in consumers:
        w.start()
    # 入队 jobs
    num_jobs = 10
    for i in range(num_jobs):
        tasks.put(Task(i,i))

    # Add a poison pill for each consumer
    for i in range(num_consumers):
        tasks.put(None)

    tasks.join()

    while num_jobs:
        result = results.get()
        print('Result:',result)
        num_jobs -= 1