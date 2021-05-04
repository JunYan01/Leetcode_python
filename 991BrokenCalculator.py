991Broken Calculator


class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        # if X >= Y:
        #     return X-Y
        
#         cache = [X]
#         count = 1
#         # return 1
#         while True:
#             cache1 = []
            
#             for x in cache:
#                 if 2*x ==Y or x-1 == Y:
#                     return count
#                 else:
#                     cache1.append(2*x)
#                     cache1.append(x-1)
#             cache = cache1
                
#             count += 1


#         s1, s2 = {X:0}, {Y:0}
#         count = 1
#         while True:
#             s1temp = {}
#             for s in s1:
#                 if 2*s in s2:
#                     return s1[s] + s2[2*s] + 1
#                 else:
#                     if 2*s not in s1:
#                         s1temp[2*s] = count
#                 if s-1 in s2:
#                     return s1[s] + s2[s-1] + 1
#                 else:
#                     if s-1 not in s1:
#                         s1temp[s-1] = count
#             s1.update(s1temp)
#             s2temp = {}
#             for s in s2:
#                 if s%2==0:
#                     if s//2 in s1:
#                         return s2[s] + s1[s//2] + 1
#                     else:
#                         if s//2 not in s2:
#                             s2temp[s//2] = count
#                 if s+1 in s1:
#                     return s2[s] + s1[s+1] + 1
#                 else:
#                     if s+1 not in s2:
#                         s2temp[s+1] = count
#             s2.update(s2temp)

#             count += 1
        # return 1
#         s1, s2 = {X:0}, {Y:0}
#         s1curr, s2curr = s1, s2
#         count = 1
#         while True:
#             s1aug = {}
#             for s in s1curr:
#                 if 2*s in s2:
#                     return s1[s] + s2[2*s] + 1
#                 else:
#                     if 2*s not in s1:
#                         s1aug[2*s] = count
#                 if s-1 in s2:
#                     return s1[s] + s2[s-1] + 1
#                 else:
#                     if s-1 not in s1:
#                         s1aug[s-1] = count
#             s1.update(s1aug)
#             s1curr = s1aug
            
#             s2aug = {}
#             for s in s2curr:
#                 if s%2==0:
#                     if s//2 in s1:
#                         return s2[s] + s1[s//2] + 1
#                     else:
#                         if s//2 not in s2:
#                             s2aug[s//2] = count
#                 if s+1 in s1:
#                     return s2[s] + s1[s+1] + 1
#                 else:
#                     if s+1 not in s2:
#                         s2aug[s+1] = count
#             s2.update(s2aug)
#             s2curr = s2aug
            
#             count += 1
        
        # print(100000//2**5)
        # print(X*2**int(math.log(Y/X,2)))
        # return math.ceil(math.log(Y/X,2))
        count = 0
        while Y>X:
            # if Y%2==1:
            #     Y+=1
            # else:
            #     Y//=2
            Y = Y + 1 if Y%2 else Y//2
            count +=1
        return count + X-Y
            
        
                

