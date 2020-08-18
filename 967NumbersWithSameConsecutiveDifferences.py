# 967. Numbers With Same Consecutive Differences


class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        # cur = range(10)
        # for i in range(N - 1):
        #     cur = {x * 10 + y for x in cur for y in [x % 10 + K, x % 10 - K] if x and 0 <= y < 10}
        #     # print(cur)
        # return list(cur)
    
        cache = []
        def traverse(pre,tail,n):
            if tail >9 or tail<0:
                return
            if n == 0:
                cache.append(pre)
                return
            
            if n-1 >= 1:
                if K>0:
                    traverse(pre*10+tail,tail+K,n-1)
                    traverse(pre*10+tail,tail-K,n-1)
                else:
                    traverse(pre*10+tail,tail,n-1)
            elif n-1 == 0:
                traverse(pre*10+tail,0,0)
        
        if N == 1:
            traverse(0,0,1)
        for i in range(1,10):
            traverse(0,i,N)
        # print(cache)

        return cache
        
        