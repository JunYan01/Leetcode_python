# TestMultipleClass.py

# class A:
#     def __init__(self,userID):
#         self.id = userID

#     def __str__(self):
#         return str(self.id)

# class B:
#     def __init__(self,userID):
#         self.aaa = A(userID//1000)

#     def __str__(self):
#         return str(self.aaa)

# a = A(200)
# print(a)

# b = B(1000)
# print(b)

# class C:

#     class A:
#         def __init__(self,userID):
#             self.id = userID
    
#         def __str__(self):
#             return str(self.id)
    
#     class B:
#         def __init__(self,userID):
#             self.aaa = C.A(userID//1000)
    
#         def __str__(self):
#             return str(self.aaa)

#     def __init__(self,user1,user2):
#         self.aaa = self.A(user1)
#         self.bbb = self.B(user2)

#     def printa(self):
#         print(self.aaa)

#     def printb(self):
#         print(self.bbb)



# a = C(200,1000)
# a.printa()

# a.printb()

# from queue import PriorityQueue

# customers = PriorityQueue() #we initialise the PQ class instead of using a function to operate upon a list. 
# # customers.put((2, "Harry"))
# # customers.put((3, "Charles"))
# # customers.put((1, "Riya"))
# # customers.put((4, "Stacy"))
# customers.put(["Harry", 2])
# customers.put(["Charles", 3])
# customers.put(["Riya", 1])
# customers.put(["Stacy", 4])
# while not customers.empty():
#      print(customers.get())
#      # print(customers.get_nowait())

try:
    import Queue as Q  # ver. < 3.0
except ImportError:
    import queue as Q

class Skill(object):
    def __init__(self, priority, description):
        self.priority = priority
        self.description = description
        print('New Level:', description)
        return
    # def __cmp__(self, other):
    #     return cmp(self.priority, other.priority)
    def __lt__(self, other):
        return self.priority < other.priority


q = Q.PriorityQueue()

q.put(Skill(5, 'Proficient'))
q.put(Skill(10, 'Expert'))
q.put(Skill(1, 'Novice'))

while not q.empty():
    next_level = q.get()
    print('Processing level:', next_level.description)



        