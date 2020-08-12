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

class C:

    class A:
        def __init__(self,userID):
            self.id = userID
    
        def __str__(self):
            return str(self.id)
    
    class B:
        def __init__(self,userID):
            self.aaa = self.A(userID//1000)
    
        def __str__(self):
            return str(self.aaa)

    def __init__(self,user1,user2):
        self.aaa = self.A(user1)
        self.bbb = self.B(user2)

    def printa(self):
        print(self.aaa)

    def printb(self):
        print(self.bbb)



a = C(200,1000)
a.printa()

a.printb()


        