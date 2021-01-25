1673  Find the Most Competitive Subsequence

class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stack = []
        for i, n in enumerate(nums):
            while stack and stack[-1] > n and i + k - len(stack) < len(nums):
                stack.pop()
            if len(stack) < k:
                stack.append(n)
        return stack
        