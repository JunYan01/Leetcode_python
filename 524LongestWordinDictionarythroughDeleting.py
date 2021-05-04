524  Longest Word in Dictionary through Deleting

class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
#         heap = []
#         heapq.heapify(heap)
#         for word in d:
#             heapq.heappush(heap,(-len(word),word))
        
#         while heap:
#             _, word = heappop(heap)
#             print(word)

        # print(sorted(d, key = lambda x: (-len(x),x),reverse = True))
    
        d.sort(key = lambda x: (-len(x),x))
        def isinString(s,x):
            i, j = 0, 0
            while i < len(s) and j <len(x):
                if s[i] == x[j]:
                    j += 1
                i += 1
            return j == len(x)
        
        for x in d:
            if isinString(s,x):
                return x
        
        return ''

#         def isinString(s,x):
#             i, j = 0, 0
#             while i < len(s) and j <len(x):
#                 if s[i] == x[j]:
#                     j += 1
#                 i += 1
#             return j == len(x)
#         output = ''
#         for x in d:
#             if isinString(s,x):
#                 output = min(output, x, key = lambda x: (-len(x),x))
        
#         return output