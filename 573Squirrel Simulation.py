# 573  Squirrel Simulation


class Solution:
    def minDistance(self, height: int, width: int, tree: List[int], squirrel: List[int], nuts: List[List[int]]) -> int:
        n = len(nuts)
        
        distance_nut_squirrel = [abs(squirrel[0]-x)+ abs(squirrel[1]-y) for x, y in nuts]
        distance_nut_tree = [abs(tree[0]-x)+ abs(tree[1]-y) for x, y in nuts]
        
        first_nut = min(range(n), key = lambda x: distance_nut_squirrel[x] - distance_nut_tree[x])
        
        return distance_nut_squirrel[first_nut] + distance_nut_tree[first_nut] + sum(distance_nut_tree[i] for i in range(n) if i != first_nut) * 2

        