# 1640. Check Array Formation Through Concatenation

class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        cache = {}
        for a in pieces:
            cache[a[0]] = a
        
        i = 0 
        while i < len(arr):
            cur = arr[i]
            if cur not in cache:
                return False
            else:
                dist = cache[cur]
                j = 0
                for j in range(len(dist)):
                    if arr[i] != dist[j]:
                        return False
                    else:
                        i += 1
        
        return True