# MaxPriorityQueueUsingMaxHeap.py

class MaxPriorityQueue(object):
	"""docstring for MaxPriorityQueue"""
	def __init__(self, n):
		super(MaxPriorityQueue, self).__init__()
		self.pq = [-1]*(n+1)
		self.n = n

	def max(self):
		return self.pq[1]

	def insert(self,value):
		self.n +=1
		self.pq.insert(self.n,value)
		self.swim(self.n)
		return

	def swim(self,k):
		while k>1 and self.less(self.parent(k),k):
			self.exchange(self.parent(k),k)
			k = self.parent(k)
		# while k>1 and less(k//2,k):
		# 	self.exchange(k//2,k)
		# 	k = k//2
		return


	def sink(self,k):
		while self.left(k) <= self.n:
			# print('start',k)
			larger = self.left(k)
			if self.right(k) <= self.n and self.less(larger,self.right(k)):
				larger = self.right(k)
			# print('mid',k,self.left(k),self.right(k),self.n)
			# print('mid',self.pq[k],self.pq[self.left(k)],self.pq[self.right(k)])
			if self.less(larger,k):
				break
			self.exchange(k,larger)
			k = larger
			# print('end',k)
		return

	def exchange(self,i,j):
		self.pq[i],self.pq[j] = self.pq[j],self.pq[i]
		return

	def less(self,i,j):
		return self.pq[i] <= self.pq[j]

	def parent(self,i):
		return i//2

	def left(self,i):
		return 2*i

	def right(self,i):
		return 2*i+1

	def display(self):
		print(self.pq)
		return

	def delMax(self):
		maxval = self.pq[1]
		self.exchange(1,self.n)
		self.pq.pop(self.n)
		self.n -= 1
		print('start to sink',self.pq[1])
		self.sink(1)
		return maxval


	
A = MaxPriorityQueue(10)
# print(A.max())
A = MaxPriorityQueue(0)
# A.insert(8)
# A.insert(10)
for i in range(6):
	A.insert(-(i-15)**2+100)
	print(-(i-15)**2+100)
	A.display()

A.display()
print(A.delMax())
A.display()

# print(A.insert())