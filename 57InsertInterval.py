# 57. Insert Interval


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # intervals = sorted(intervals,key = lambda x: x[0])
        # intervals.sort(key = lambda x: x[0])
        # print(intervals)
        
#         n = len(intervals)
#         if n == 0:
#             return [newInterval]
#         res = []
#         i = 0
#         while i < n and intervals[i][1]<newInterval[0]:
#             res.append(intervals[i])
#             i += 1
#         l,r = newInterval
#         while i < n and intervals[i][0] <= newInterval[1]:
#             l = min(l,intervals[i][0])
#             r = max(r,intervals[i][1])
#             i += 1
#         res.append([l,r])
#         res.extend(intervals[i:])
        
#         return res
        
        n = len(intervals)
        if n == 0:
            return [newInterval]
        
        i = 0
        l,r = newInterval
        while i < n and intervals[i][1]<newInterval[0]:
            i += 1
        
        while i < n and intervals[i][0] <= newInterval[1]:
            l = min(l,intervals[i][0])
            r = max(r,intervals[i][1])
            intervals.pop(i)
            n -= 1
        intervals.insert(i,[l,r])
        
        return intervals
                