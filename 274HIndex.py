# 274. H-Index

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        # print(citations)
        n = len(citations)
        if n == 0:
            return 0
        
        h = n
        if citations[n-h]>=h:
            return h
        
        
        for h in range(n-1,-1,-1):
            if n>n-h-1>=0 and citations[n-h-1] <= h and n>n-h >=0 and citations[n-h] >= h:
                break
        
        
        return h
                
        