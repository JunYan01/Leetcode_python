916Word Subsets

class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
#         from huahua
        def getCount(word):
            count = dict()
            for w in word:
                count[w] = count.get(w,0) + 1
            return count
        
        req = dict()
        for b in B:
            cur = getCount(b)
            for x in cur:
                req[x] = max(req.get(x,0), cur[x])
        
        # print(req)
        ans = []
        for a in A:
            cur = getCount(a)
            if all(req[x]<=cur.get(x,0) for x in req):
                ans.append(a)
                
        return ans