# 489. Robot Room Cleaner


# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        def goBack(robot):
            robot.turnLeft()
            robot.turnLeft()
            robot.move()
            robot.turnRight()
            robot.turnRight()
        
        def dfs(pos, robot, d, visited):
            if pos in visited:
                return
            visited.append(pos)
            
            robot.clean()
            
            for _ in directions: 
                if robot.move():
                    dfs([pos[0]+directions[d][0],pos[1]+directions[d][1]],robot,d, visited)
                    goBack(robot)
                robot.turnRight()
                d = (d+1)%len(directions)
        
        dfs([0,0],robot,0,[])



#         directions = [(0,1), (1,0), (0,-1), (-1,0)]
#         def goBack(robot):
#             robot.turnLeft()
#             robot.turnLeft()
#             robot.move()
#             robot.turnRight()
#             robot.turnRight()
        
#         def dfs(pos, robot, d, visited):
#             if pos in visited:
#                 return
#             visited.add(pos)
            
#             robot.clean()
#             for _ in directions: 
#                 if robot.move():
#                     dfs((pos[0]+directions[d][0],pos[1]+directions[d][1]),robot,d, visited)
#                     goBack(robot)
#                 robot.turnRight()
#                 d = (d+1)%len(directions)
        
#         dfs((0,0),robot,0,set())

        # visited = set()
        # dfs((0,0),robot,0,visited)
        # print(visited)
        

#         def go_back():
#             robot.turnRight()
#             robot.turnRight()
#             robot.move()
#             robot.turnLeft()
#             robot.turnLeft()
            
#         def backtrack(cell = (0, 0), d = 0):
#             visited.add(cell)
#             robot.clean()
#             # going clockwise : 0: 'up', 1: 'right', 2: 'down', 3: 'left'
#             for i in range(4):
#                 new_d = (d + i) % 4
#                 new_cell = (cell[0] + directions[new_d][0], \
#                             cell[1] + directions[new_d][1])
                
#                 if not new_cell in visited and robot.move():
#                     backtrack(new_cell, new_d)
#                     go_back()
#                 # turn the robot following chosen direction : clockwise
#                 robot.turnRight()
    
#         # going clockwise : 0: 'up', 1: 'right', 2: 'down', 3: 'left'
#         directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
#         visited = set()
#         backtrack()
#         print(visited)
        