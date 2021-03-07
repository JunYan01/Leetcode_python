from multiprocessing import Process
import os

a, b, c, d = 1, 2, 3, 4

# 子进程要执行的代码
def sum1(name):
    global a, b, c
    print('Run child process %s (%s)...' % (name, os.getpid()))
    a = a + 1 + c
    print(a)

def sum2(name):
    global a, c, d
    print('Run child process %s (%s)...' % (name, os.getpid()))
    a = a + 2
    c = c + d

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=sum1, args=('a + b',))
    q = Process(target=sum2, args=('c + d',))
    print('Child process will start.')
    p.start()
    q.start()
    q.join()
    p.join()
    print('Child process end.')
    print(a)