# 1291. Sequential Digits


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
#         n = low
#         k = 0
#         while n:
#             k +=1
#             n = n//10
#         n = high
#         l = 0
#         while n:
#             l +=1
#             n = n//10
#         l = 9 if l >= 10 else l
#         # print(k,l)
#         arr = []
#         for l in range(k,l+1):
#             value = 0
#             value1 = 0
#             for n in range(1,l):
#                 value += n
#                 value *= 10
#                 value1 += 1
#                 value1 *= 10
#             value += l
#             value1 += 1
#             # print(value)
#             if value >= low and value <= high:
#                 arr.append(value)
#             for n in range(l+1,10):
#                 value += value1
#                 if value > high:
#                     return arr
#                 if value >= low:
#                     arr.append(value)
#             # print(arr)
#         return arr
        seq = "123456789"
        res = []
        for l in range(1,10):
            if int(seq[9-l:9]) < low:
                continue
            for i in range(10-l):
                num = int(seq[i:i+l])
                if num > high:
                    return res
                if num >= low:
                    res.append(num)       
        return res