322  Coin Change

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
#         num = [float('inf')]*(amount+1)
#         num[0] = 0
#         for i in range(1,amount+1):
#             for c in coins:
#                 if i - c>=0:
#                     num[i] = min(num[i],num[i-c] + 1)
#         return num[amount] if num[amount]  != float('inf') else -1

        # num = [-1]*(amount+1)
        # num[0] = 0
        # for i in range(1,amount+1):
        #     for c in coins:
        #         if i - c>=0 and num[i-c] != -1:
        #             if num[i] == -1:
        #                 num[i] = num[i-c] + 1
        #             else:
        #                 num[i] = min(num[i],num[i-c] + 1)
        # return num[amount]
        queue.append((0,0))
        while True:
            val, num = queue.pop(0)
            for queue.