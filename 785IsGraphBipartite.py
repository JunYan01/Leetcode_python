785  Is Graph Bipartite?
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
# DFS with recursion        
#         m = len(graph)
#         colors = [0] * m
        
#         def coloring(k,color):
#             if colors[k]:
#                 return colors[k] == color
#             colors[k] = color
#             for l in graph[k]:
#                 if not coloring(l, - color):
#                     return False
#             return True
        
#         for k in range(m):
#             if not colors[k] and not coloring(k,1):
#                 return False

#         return True

# This is actually BFS
#         m = len(graph)
#         colors = [0] * m
        
#         def coloring(k,color):
#             colors[k] = color
#             queue = [(k,color)]
#             while queue:
#                 l, c = queue.pop(0)
#                 for m in graph[l]:
#                     if colors[m] == c:
#                         return False
#                     elif colors[m] == 0:
#                         colors[m] = -c
#                         queue.append((m,-c))
#                     elif colors[m] == -c:
#                         continue
#                     else:
#                         print('Error!')
            
#             return True
        
#         for k in range(m):
#             if not colors[k] and not coloring(k,1):
#                 print(colors)
#                 return False
#         print(colors)
#         return True


# DFS without recursion
        m = len(graph)
        colors = [0] * m
        
        def coloring(k,color):
            colors[k] = color
            stack = [(k,color)]
            while stack:
                l, c = stack[-1]
                if graph[l]:
                    m = graph[l].pop()
                    if colors[m] == c:
                        return False
                    elif colors[m] == 0:
                        colors[m] = -c
                        stack.append((m,-c))
                    elif colors[m] == -c:
                        continue
                    else:
                        print('Error!')
                else:
                    stack.pop()
            
            return True
        
        for k in range(m):
            if not colors[k] and not coloring(k,1):
                print(colors)
                return False
        print(colors)
        return True
        