# 1165  Single-Row Keyboard

class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        dic = dict(zip(keyboard,range(26)))
        index = 0
        val = 0
        for w in word:
            # print(val)
            index1 = dic[w]
            val += abs(index1-index)
            index = index1
            # print(val)
        return val
            

if __name__ == '__main__':
    solution = Solution()
    print(solution.calculateTime('adfadfadf','dfa'))
    import math

    print(math.sin(30))