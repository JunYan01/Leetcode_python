784Letter Case Permutation

class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        # cache = ['']
        # for s in S:
        #     if s.isalpha():
        #         # cache1 = [x+s.lower()  for x in cache]
        #         # cache1.extend([x+s.upper()  for x in cache])
        #         cache1 = [x+s.lower()  for x in cache] + [x+s.upper()  for x in cache]
        #         # cache1 = list(map(lambda x: (x+s.lower(),x+s.upper()), cache))
        #         # cache1.extend(list(map(lambda x: x+s.upper(), cache)))
        #     else:
        #         cache1 = [x+s for x in cache]
        #     cache = cache1
        # # print(cache)
        # return cache
        cache = ['']
        for s in S:
            if s.isalpha():
                # cache = [x+s.lower()  for x in cache] + [x+s.upper()  for x in cache]
                cache = [y for x in cache for y in [x+s.lower(),x+s.upper()] ] 
            else:
                cache = [x+s for x in cache]
        return cache