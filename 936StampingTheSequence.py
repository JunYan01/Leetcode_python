936Stamping The Sequence

class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        
        def unStamp(stamp, target, s):
            l = len(stamp)
            for i in range(len(stamp)):
                if target[s+i] == '*':
                    l -= 1
                elif target[s+i] != stamp[i]:
                    return 0
            if l != 0:
                # print(l,target[s:s+len(stamp)])
                target[s:s+len(stamp)] = ['*']*len(stamp)
                # target = target[:s] + '*'*l + target[s+l:]
            return l
        
        n = len(target)
        m = len(stamp)
        ans = []
        seen = [0]*n
        total = 0
        target = list(target)
        while total < n:
            found = False
            for i in range(n-m+1):
                if seen[i]: continue
                l = unStamp(stamp, target, i)
                if l == 0: continue
                seen[i] = 1
                total += l
                ans.insert(0,i)
                found = True
            # print(target,l,found)
            if not found: return []
        
        return ans
        