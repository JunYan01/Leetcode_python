1136  Parallel Courses

class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        """
        :type N: int
        :type relations: List[List[int]]
        :rtype: int
        """

        graph = defaultdict(dict)
        temp = defaultdict(dict)

        for i, j in relations:
            graph[i][j] = 1
            temp[j][i] = 1
        indegree = {j: len(temp[j]) for j in temp}
        for i in range(1, n + 1):
            if i not in indegree:
                indegree[i] = 0

        count = 0

        while len(indegree) > 0:
            temp = dict(indegree)
            pop_node = [i for i in temp if temp[i] == 0]
            for i in pop_node:
                for j in graph[i]:
                    temp[j] -= 1
                del (temp[i])
            if len(temp) > 0 and temp == indegree:
                return -1
            else:
                indegree = temp
                count += 1
        return count
        # courses = n
        # visited = [False for i in range(n+1)]
        # queue = []
        # graph = [[] for i in range(n+1)]
        # in_degree = [0 for i in range(n+1)]
        # for i in relations:
        #     graph[i[0]].append(i[1])
        #     in_degree[i[1]]+=1
        # semeseter = 1
        # for i in range(1,n+1):
        #     if not in_degree[i]:
        #         queue.append(i)
        #         visited[i] = True
        #     semester = 1
        #     courses -= len(queue)
        #     while queue and courses:
        #         current_size = len(queue)
        #         while current_size:
        #             current_course = queue[0]
        #             queue.pop(0)
        #             current_size-=1
        #             for i in graph[current_course]:
        #                 in_degree[i]-=1
        #                 if not visited[i] and not in_degree[i]:
        #                     courses-=1
        #                     queue.append(i)
        #                 visited[i]=True
        #         semester+=1
        # return semester if not courses else -1
        
#         # S = 1<<n
#         S = 7
#         print('1'.split(str(bin(S))))
#         print(len('1'.split(str(bin(S)))))
#         deps = [[]]*n
#         for d in dependencies:
#             deps[d[1] - 1] = 1 << ( d[0] - 1)
#         dp = [[]]*S
#         dp[0] = 1
#         for d in range(1,n+1):
#             tmp = [[]]*S
#             for s in range(S):
#                 if not dp[s]: continue
#                 mask = 0
#                 for i in range(n):
#                     if not (s and (1<<i)) && (s & deps[i]) == deps[i]:
#                         mask |= (1<<i)
#                 if str(bin(mask))<= k:
                    
#         # print(S,deps)
#         return 0