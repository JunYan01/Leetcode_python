# 470. Implement Rand10() Using Rand7()


# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        while True:
            # a, b = rand7(), rand7()
            res = rand7()+ (rand7()-1)*7
            if res<=40:
                return res%10+1