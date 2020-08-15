# Power of Eight
# If we want power of Eight
# Bit Manipulation + Math

class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        return num > 0 and num & (num - 1) == 0 and num % 7 == 1


