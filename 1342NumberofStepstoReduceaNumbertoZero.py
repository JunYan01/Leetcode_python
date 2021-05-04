1342Number of Steps to Reduce a Number to Zero    
class Solution:
    def numberOfSteps (self, num: int) -> int:
#         if not num:
#             return num
#         count = 0
        
#         while num>1:
#             print(num)
#             count += 1 + num%2
#             num >>= 1
#             # count +=1
#         return count + 1

        if not num:
            return num
        count = 0
        while num:
            print(num)
            count += 1 + num%2
            num >>= 1
        return count - 1