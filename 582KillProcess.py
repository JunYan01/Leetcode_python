582  Kill Process

class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
#         cache = {}
#         n = len(pid)
#         for i in range(n):
#             # if ppid[i] in cache:
#             #     cache[ppid[i]].append(pid[i])
#             # else:
#             #     cache[ppid[i]] = [pid[i]]
        
#         queue = [kill]
# #         BFS
#         record = []
#         while queue:
#             k = queue.pop(0)
#             record.append(k)
#             if k in cache:
#                 queue.extend(cache[k])
        
#         return record
        cache = defaultdict(list)
        n = len(pid)
        for i in range(n):
            cache[ppid[i]].append(pid[i])
        
        queue = [kill]
#         BFS
        record = [kill]
        while queue:
            k = queue.pop(0)
            if k in cache:
                queue.extend(cache[k])
                record.extend(cache[k])
        
        return record