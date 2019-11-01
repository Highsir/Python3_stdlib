import signal
import os
import time

def do_exit(sig,stack):
    raise SystemError('Exiting')

signal.signal(signal.SIGINT,signal.SIG_IGN)
signal.signal(signal.SIGUSR1,do_exit)

print('mypid:',os.getpid())
signal.pause()