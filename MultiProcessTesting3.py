from multiprocessing import Pool
import os, time, random
# Only works for Unix/Linux/Mac

def long_time_task(name):
	print('Run task %s (%s)...' % (name, os.getpid()))
	start = time.time()
	time.sleep(random.random()*3)
	end = time.time()
	print('Task %s run %0.2f seconds.' % (name, (end - start)))

if __name__ == '__main__':
	print('Parent process %s.' % os.getpid())
	m, n = 4, 5
	p = Pool(m)
	for i in range(n):
		p.apply_async(long_time_task, args = (i,))
	print('Waiting for all subprocesses done...')
	p.close()
	p.join()
	print('All subprocesses done.')

# from multiprocessing import Pool
# import os, time, random

# def long_time_task(name):
#     print('Run task %s (%s)...' % (name, os.getpid()))
#     start = time.time()
#     time.sleep(random.random() * 3)
#     end = time.time()
#     print('Task %s runs %0.2f seconds.' % (name, (end - start)))

# if __name__=='__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Pool(4)
#     for i in range(5):
#         p.apply_async(long_time_task, args=(i,))
#     print('Waiting for all subprocesses done...')
#     p.close()
#     p.join()
#     print('All subprocesses done.')