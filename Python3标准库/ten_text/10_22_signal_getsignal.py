import signal


def alarm_received(n,stack):
    return

signal.signal(signal.SIGALRM,alarm_received)

signal_to_names = {
    getattr(signal,n): n for n in dir(signal)
    if n.startswith('SIG') and '_' not in n
}

for s,name in sorted(signal_to_names.items()):
    handler = signal.getsignal(s)
    if handler is signal.SIG_DFL:
        handler = 'SIG_DEL'
    elif handler is signal.SIG_IGN:
        handler = 'SIG_IGN'
    print('{:<8} ({:2d})'.format(name,s),handler)