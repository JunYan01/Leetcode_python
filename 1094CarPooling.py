# 1094. Car Pooling

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # trips = sorted(trips, key = lambda x: x[1])
        # print(trips)
        # index = [x[0] for x in sorted(enumerate(trips), key = lambda x: x[1][2])]
        # print(index)
        # last = sorted(trips, key = lambda x: x[2])
        # print(last)
        # # index = sorted(range(len(trips)), key=lambda k: trips[k][2])
        # # print(index)
        # # last = sorted(trips, key = lambda x: x[2])
        # # print(last)
        
        # pick, drop = [], []
        # for t in trips:
        #     pick.append((t[1], t[0]))
        #     drop.append((t[2], t[0]))
        # pick.sort()
        # drop.sort()
        # p = d = cur = 0
        # while p < len(trips) and d < len(trips):
        #     pickTime, pickNum = pick[p]
        #     dropTime, dropNum = drop[d]
        #     if pickTime < dropTime:
        #         cur += pickNum
        #         if cur > capacity:
        #             return False
        #         p += 1
        #     else:
        #         cur -= dropNum
        #         d += 1
        
        pos = [0]* 1001
        for trip in trips:
            pos[trip[1]] += trip[0]
            pos[trip[2]] -= trip[0]
        curr = 0
        for diff in pos:
            curr += diff
            if curr > capacity:
                return False
        return True
        
        return True