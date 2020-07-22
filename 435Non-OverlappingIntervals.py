# 435. Non-overlapping Intervals


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
#         # print(sorted(intervals, key = lambda x: x[1]))
#         intervals.sort(key = lambda x: x[1])       
#         # print(intervals)
#         n = len(intervals)
#         if n <1:
#             return 0
#         j = 0
#         count = 1
#         end = intervals[j][1]
#         j += 1
#         while j<n:
#             if intervals[j][0]< end:
#                 j += 1
#                 continue
#             end = intervals[j][1]
#             count += 1
#             j += 1
#         return n-count

        # print(sorted(intervals, key = lambda x: x[1]))
        intervals.sort(key = lambda x: x[1])       
        # print(intervals)
        n = len(intervals)
        if n <1:
            return 0
        count = 0
        end = float('-inf')
           
        for j in range(n):
            if intervals[j][0] >= end:
                end = intervals[j][1]
                count += 1
                # print(j,count)
            
        return n-count    
    
        