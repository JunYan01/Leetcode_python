# 58. Length of Last Word

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # ct = 0
        # flag = False
        # for l in s:
        #     if l == ' ':
        #         flag = True
        #     else:
        #         if flag == True:
        #             ct = 0
        #             flag = False
        #         ct += 1
        # return ct
        
        # ct = ctl = 0
        # for l in s:
        #     if l == ' ':
        #         ct = 0
        #     else:
        #         ct += 1
        #         ctl = ct
        # return ctl
        
        # s = s.strip()
        # return len(s.split()[-1] if s else 0)
        