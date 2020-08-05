# 342. Power of Four

# return num > 0 and num & (num - 1) == 0 and num % 7 == 1
# If we want power of Eight
# Bit Manipulation + Math

class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        return num > 0 and num & (num - 1) == 0 and num % 3 == 1

        # return num > 0 and num & (num - 1) == 0 and num & 0xaaaaaaaa == 0

        # if num<1:
        #     return False
        # return num == (4**int(log(num)/log(4)))
    
        # return num > 0 and log2(num) % 2 == 0

        # if num < 1:
        #     return False
        # while num %4 == 0:
        #     # print(num)
        #     num /= 4
            
        # # print(num)
        # return num == 1
    