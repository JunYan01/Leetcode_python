# 1103. Distribute Candies to People


class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        # print(sqrt(candies))
        # return []
#         n = int(sqrt(candies*2))+1
#         while n*(n+1)//2 > candies:
#             n = n-1
#         print(n)
#         j, k = divmod(n, num_people)
#         # print(j,k)
#         # print(candies - n*(n+1)//2)
#         res = [0] *num_people
#         if k > 0:
#             for i in range(k):
#                 res[i] = (i+1+j*num_people+i+1)*(j+1)//2
#                 # print(i+1,j*num_people+i+1,j+1,res[i])
#             for i in range(k,num_people):
#                 res[i] = (i+1+(j-1)*num_people+i+1)*(j)//2
#             # print(res,candies - n*(n+1)//2)
#             res[k] += candies - n*(n+1)//2
#         else:
#             for i in range(num_people):
#                 res[i] = (i+1+(j-1)*num_people+i+1)*(j)//2
#             print(res,candies - n*(n+1)//2)
#             res[0] += candies - n*(n+1)//2
        
#         return res

#         n = int(sqrt(candies*2))+1
#         while n*(n+1)//2 > candies:
#             n -= 1
#         print(n)
#         j, k = divmod(n, num_people)
#         # print(j,k)
#         # print(candies - n*(n+1)//2)
#         res = [0] *num_people
#         for i in range(k):
#             res[i] = (i+1+j*num_people+i+1)*(j+1)//2
#         for i in range(k,num_people):
#             res[i] = (i+1+(j-1)*num_people+i+1)*(j)//2
#         res[k] += candies - n*(n+1)//2
        
        
#         return res

        n = int(sqrt(candies*2))+1
        while n*(n+1)//2 > candies:
            n -= 1
        # print(n)
        j, k = divmod(n, num_people)
        res = [0] *num_people
        curr = (0+1+j*num_people+0+1)*(j+1)//2
        for i in range(k):
            res[i] = curr
            curr += j+1
        curr =  (k+1+(j-1)*num_people+k+1)*(j)//2
        for i in range(k,num_people):
            res[i] = curr
            curr += j
        res[k] += candies - n*(n+1)//2
        
        return res
        
        
        # res = [0] *num_people
        # current = 1
        # i = 0
        # while candies > current:
        #     res[i%num_people] += current
        #     # print(i%num_people,res[i%num_people])
        #     candies -= current
        #     i += 1
        #     current += 1
        # res[i%num_people] += candies
        # return res
    
        # res = [0] * num_people
        # i = 0
        # while candies > 0:
        #     res[i % num_people] += min(candies, i + 1)
        #     candies -= i + 1
        #     i += 1
        # return res
    
    
        