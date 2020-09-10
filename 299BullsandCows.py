# 299. Bulls and Cows


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
#         a = 0
#         b = 0
#         cache = []
        
#         for i,l in enumerate(guess):
#             if l == secret[i]:
#                 a +=1
#             else:
#                 cache.append(secret[i])
#         for i,l in enumerate(guess):
#             if l != secret[i] and l in cache:
#                 b += 1
#                 cache.remove(l)
#             # print(cache)
#         # print(a,b)
#         return str(a)+'A'+str(b)+'B'

        # s1, s2 = defaultdict(int), defaultdict(int)
        # A = B = 0
        # for s,g in zip(secret, guess):
        #     if s == g:
        #         A += 1
        #     else:
        #         s1[s] += 1
        #         s2[g] += 1
        # for k in s1:
        #     if k in s2:
        #         B += min(s1[k], s2[k])
        # return "%sA%sB" % (A,B)
        
        s1, s2 = {}, {}
        A = B = 0
        for s,g in zip(secret, guess):
            if s == g:
                A += 1
            else:
                s1[s] = s1.get(s,0) +1
                s2[g] = s2.get(g,0) +1
        for k in s1:
            if k in s2:
                B += min(s1[k], s2[k])
        return "%sA%sB" % (A,B)
        
        