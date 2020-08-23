# 497. Random Point in Non-overlapping Rectangles


class Solution:

#     def __init__(self, rects: List[List[int]]):
#         self.rects = rects
#         self.areas = [(rx - lx + 1) * (ry - ly + 1) for lx, ly, rx, ry in rects]
#         self.sum = sum(self.areas)

#     def pick(self) -> List[int]:
#         import random

#         rand = random.randint(0, self.sum)
#         sm = 0
#         for i, area in enumerate(self.areas):
#             sm += area
#             if rand <= sm:
#                 rect = self.rects[i]
#                 return [random.randrange(rect[0], rect[2] + 1), random.randrange(rect[1], rect[3] + 1)]
# 链接：https://leetcode-cn.com/problems/random-point-in-non-overlapping-rectangles/solution/497-fei-zhong-die-ju-xing-zhong-de-sui-ji-dian-by-/


        def __init__(self, rects):
            self.rects, self.ranges, sm = rects, [], 0
            for x1, y1, x2, y2 in rects:
                sm += (x2 - x1 + 1) * (y2 - y1 + 1)
                self.ranges.append(sm)

        def pick(self):
            x1, y1, x2, y2 = self.rects[bisect.bisect_left(self.ranges, random.randint(1,self.ranges[-1]))]
            return [random.randint(x1, x2), random.randint(y1, y2)]

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()