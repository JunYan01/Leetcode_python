# 594  Longest Harmonious Subsequence

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        frequency = defaultdict(int)
        for n in nums:
            frequency[n] += 1
        # print(sorted(frequency.keys()))
        digits = sorted(frequency.keys())
        print(digits)
        count = 0
        for i in range(len(digits)-1):
            if digits[i+1] == digits[i]+1:
                count = max(count,frequency[digits[i]]+frequency[digits[i+1]])
        return count