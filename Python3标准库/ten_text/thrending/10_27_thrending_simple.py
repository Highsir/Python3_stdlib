import threading

def Woker(num):
    print('Woker: %s' % num)

threads = []
for i in range(5):
    t = threading.Thread(target=Woker,args=(i,))
    threads.append(t)
    t.start()