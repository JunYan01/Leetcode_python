# 1041. Robot Bounded In Circle


class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
#         deg = [[0,1],[1,0],[0,-1],[-1,0]]
#         pos = [0,0]
#         angle = 1
#         def result(pos,angle,instructions):
#             # print(pos,angle)
#             init = angle
#             initP = pos[:]
#             for step in instructions:
#                 if step == "G":
#                     pos[0], pos[1] = pos[0] + deg[angle][0], pos[1] + deg[angle][1]
#                 elif step == 'L':
#                     angle = angle + 1 if angle < 3 else 0
#                 elif step == 'R':
#                     angle = angle - 1 if angle > 0 else 3
#             # print(pos,angle)
#             # print(initP == pos)
#             # print(init != angle)
#             return initP == pos or init != angle
        
#         return result(pos,angle,instructions)
        
#         deg = [[0,1],[1,0],[0,-1],[-1,0]]
#         pos = [0,0]
#         angle = 1
#         def result(pos,angle,instructions):
#             # print(pos,angle)
#             initP = pos[:]
#             for _ in range(4):
#                 for step in instructions:
#                     if step == "G":
#                         pos[0], pos[1] = pos[0] + deg[angle][0], pos[1] + deg[angle][1]
#                     elif step == 'L':
#                         angle = angle + 1 if angle < 3 else 0
#                     elif step == 'R':
#                         angle = angle - 1 if angle > 0 else 3
#             # print(pos,angle)
#             # print(initP == pos)
#             # print(init != angle)
#             return initP == pos
        
#         return result(pos,angle,instructions)

        x = y = 0
        d = (0,1)
        for c in instructions:
            if c == 'G':
                x, y = x + d[0], y + d[1]
            elif c == 'L':
                d = (-d[1],d[0])
            else:
                d = (d[1],-d[0])
        return (x == 0 and y == 0) or d != (0,1)