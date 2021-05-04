1337  The K Weakest Rows in a Matrix

import heapq 
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        # m, n = len(mat), len(mat[0])
        # # cache = defaultset()
        # cache = {}
        # for i in range(m):
        #     t = sum(mat[i])
        #     if t in cache:
        #         cache[t].append(i)
        #     else:
        #         cache[t]= [i]
        # # print(cache)
        # arr = []
        # for i in sorted(cache.keys()):
        #     print(i,cache[i])
        #     arr.extend(cache[i])
        #     if len(arr)>=k:
        #         return arr[:k]
        
        m, n = len(mat), len(mat[0])
        cache = {}
        heap = []
        heapq.heapify(heap)
        currMax = n
        for i in range(m):
            t = sum(mat[i])
            if t in cache:
                cache[t].append(i)
            elif t not in cache and t <= currMax:
                cache[t]= [i]
                # print(t)
                if len(heap)<k:
                    heapq.heappush(heap, -t)
                else:
                    # print(t)
                    if t < -heap[0]:
                        del cache[-heap[0]]
                        currMax = min(-heap[0],currMax)
                        heapq.heapreplace(heap, -t)
                        
        


        print(cache)
        arr = []
        while heap:
            i = - heapq.heappop(heap)
            # for i in sorted(cache.keys()):
            print(i,cache[i])
            arr = cache[i] + arr
            # if len(arr)>=k:
            #     return arr[:k]
        return arr[:k]
            