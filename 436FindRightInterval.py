# 436. Find Right Interval


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        # intervals = sorted((e[0], i , e[1]) for i, e in enumerate(intervals))
        # l = len(intervals)
        # res = [0] * l
        # for e in intervals:
        #     r = bisect.bisect_left(intervals, (e[2], ))
        #     res[e[1]] = intervals[r][1] if r<l else -1
        # return res
        
        # intervals = sorted([[e[0], e[1], i ] for i, e in enumerate(intervals)],key = lambda x:x[0])
        l = len(intervals)
        res = [-1] * l
        intervals = sorted([[e[0], e[1], i ] for i, e in enumerate(intervals)])
        # print(intervals) 
        for e in intervals:
            # print(e)
            r = bisect.bisect_left(intervals, [e[1], ])
            res[e[2]] = intervals[r][2] if r<l else -1
        return res