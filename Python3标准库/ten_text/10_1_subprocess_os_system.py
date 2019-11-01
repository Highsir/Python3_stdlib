import subprocess
import sys
import os
import time
import signal

# completed = subprocess.run(['ls','-1'])
# print('returncode:',completed.returncode)

# completed = subprocess.run('echo $HOME',shell=True)
# print('returncode:',completed.returncode)
#
# try:
#     subprocess.run(['false'],check=True)
# except subprocess.CalledProcessError as err:
#     print('ERROR:',err)

# completed = subprocess.run(['ls','-1'],stdout=subprocess.PIPE)
# print('HAVE {} bytes in stdout:\n{}'.format(len(completed.stdout),completed.stdout.decode('utf-8')))
# print('returncode:',completed.returncode)


# try:
#     completed = subprocess.run(
#         'echo to stdout; echo to stderr 1>&2; exit 1',
#         check=True,
#         shell=True,
#         stdout=subprocess.PIPE,
#     )
# except subprocess.CalledProcessError as err:
#     print('ERROR:',err)
# else:
#     print('returncode:',completed.returncode)
#     print('HAVE {} bytes in stdout:\n{}'.format(len(completed.stdout),completed.stdout.decode('utf-8')))
# #
# try:
#     output = subprocess.check_output(
#         'echo to stdout; echo to stderr 1>&2',
#         shell=True,
#         stderr=subprocess.STDOUT,
#     )
# except subprocess.CalledProcessError as err:
#     print('ERROR:', err)
# else:
#     print('HAVE {} bytes in stdout:\n{!r}'.format(len(output), output.decode('utf-8')))

# print('read:')
# proc = subprocess.Popen(
#     ['echo','"to stdout"'],
#     stdout=subprocess.PIPE
# )
# stdout_value = proc.communicate()[0].decode('utf-8')
# print('stdout:',repr(stdout_value))


# print('popen2:')
# proc = subprocess.Popen(
#     ['cat','-'],
#     stdin=subprocess.PIPE,
#     stdout=subprocess.PIPE,
#
# )
# msg = 'through stdin to stdout'.encode('utf-8')
# stdout_value = proc.communicate(msg)[0].decode('utf-8')
# print('pass through:',repr(stdout_value))

# sys.stderr.write('repeater.py:starting\n')
# sys.stderr.flush()
# while True:
#     next_line = sys.stdin.readline()
#     print(next_line)
#     sys.stderr.flush()
#     if not next_line:
#         break
#     sys.stdout.write(next_line)
#     sys.stdout.flush()
#
# sys.stderr.write('repeater.py: exiting\n')
# sys.stderr.flush()

proc = subprocess.Popen(['python3','signal_child.py'])
print('PARENT:Pausing before sending signal..')
sys.stdout.flush()
time.sleep(1)
print('PARENT:Singnal child')
sys.stdout.flush()
os.kill(proc.pid,signal.SIGUSR1)