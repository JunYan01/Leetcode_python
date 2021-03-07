from multiprocessing import Process
import os, multiprocessing

a = multiprocessing.Value("d", 1)
b = multiprocessing.Value("d", 2)
c = multiprocessing.Value("d", 3)
d = multiprocessing.Value("d", 4)

# 数组型：num=multiprocessing.Array("i",[1,2,3,4,5])
# 字典：mydict=multiprocessing.Manager().dict()
# 列表：mylist=multiprocessing.Manager().list(range(5))

# 子进程要执行的代码

def sum1(name):
    global a, b, c
    print('Run child process %s (%s)...' % (name, os.getpid()))
    a.value = a.value + 1 + c.value

def sum2(name):
    global a, c, d
    print('Run child process %s (%s)...' % (name, os.getpid()))
    a.value = a.value + 2
    c.value = c.value + d.value

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
    print(a.value)