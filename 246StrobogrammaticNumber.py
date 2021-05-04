246  Strobogrammatic Number

class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        # non = set([2, 3, 4, 5, 7])
        # proj = {0:0,1:1,6:9,8:8,9:6}
        # res = ''
        # for i in num[::-1]:
        #     integer = int(i)
        #     # print(integer)
        #     if integer in non:
        #         return False
        #     res += str(proj[integer])
        # print(res)
        # return res == num
        
        # proj = {0:0,1:1,6:9,8:8,9:6}
        # i, j = 0, len(num) - 1
        # while i <= j:
        #     x, y = int(num[i]), int(num[j])
        #     if x not in proj or y not in proj or x != proj[y]:
        #         return False
        #     i+=1
        #     j-=1
        # return True
        
        proj = {0:0,1:1,6:9,8:8,9:6}
        i, j = 0, len(num) - 1
        while i <= j:
            x, y = int(num[i]), int(num[j])
            if x not in proj or y not in proj or x != proj[y]:
                return False
            i+=1
            j-=1
        return True