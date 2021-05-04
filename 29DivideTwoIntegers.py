29Divide Two Integers

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2147483648 and divisor == -1:
            return 2147483647
        sign = -1 if ((dividend < 0)^(divisor <0)) else 1
        dividend = abs(dividend)
        divisor = abs(divisor)
        quotient = 0
        temp = 0
        
        for i in range(31,-1,-1):
            if (temp + (divisor << i) <= dividend):
                temp += divisor << i
                quotient |= 1 << i
        return quotient if sign > 0 else -quotient
        # if dividend == 0:
        #     return 0
        # if max(dividend, divisor) < 0 or min(dividend, divisor) > 0:
        #     isPositive = True
        # else:
        #     isPositive = False
        # dividend = -dividend if dividend < 0 else dividend
        # divisor = -divisor if divisor < 0 else divisor
        # count = 0
        # while dividend >= divisor:
        #     count += 1
        #     dividend -= divisor
        # return count if isPositive else -count
#         if dividend == 0:
#             return 0
#         if divisor == 1:
#             return dividend
#         if divisor == -1:
#             return -dividend
#         if dividend < divisor:
#             return 0
#         if max(dividend, divisor) < 0 or min(dividend, divisor) > 0:
#             isPositive = True
#         else:
#             isPositive = False
#         dividend = -dividend if dividend < 0 else dividend
#         divisor = -divisor if divisor < 0 else divisor
#         count = 0
#         cache = []
#         temp = divisor
#         while dividend >= temp:
#             cache.append(temp)
#             temp += temp
#             count += 1
        
#         res = 0
#         print(cache)
        
#         for i in range(count,-1,-1):
#             if dividend >= cache[i-1]:
#                 res += 1 << (i-1)
#                 dividend -= cache[i-1]
#                 print(1 << (i-1))
        
#         return res if isPositive else -res