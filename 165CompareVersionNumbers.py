# 165. Compare Version Numbers


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
#         version1 = [int(x) for x in version1.split('.')]
#         version2 = [int(x) for x in version2.split('.')]

#         if len(version1) > len(version2):
#             version2.extend([0]*(len(version1)-len(version2)))
#         else:
#             version1.extend([0]*(len(version2)-len(version1)))

#         for i in range(len(version1)):
#             if version1[i] > version2[i]:
#                 return 1
#             elif version1[i] < version2[i]:
#                 return -1
#         return 0
        
#         n1 = len(version1)
#         n2 = len(version2)
        
#         version1 = [int(x) for x in version1.split('.')]
#         version2 = [int(x) for x in version2.split('.')]
        
#         while version2 or version1:
#             try:
#                 v2 = version2.pop(0)
#             except:
#                 v2 = 0
                
#             try:
#                 v1 = version1.pop(0)
#             except:
#                 v1 = 0
            
#             if v1 > v2:
#                 return 1
#             elif v1 < v2:
#                 return -1
            
#         return 0
        v1, v2 = version1.split('.'), version2.split('.')
        n1, n2 = len(v1), len(v2)
        
        for i in range(max(n1,n2)):
            p1 = int(v1[i]) if i<n1 else 0
            p2 = int(v2[i]) if i<n2 else 0
            if p1 > p2:
                return 1
            elif p1 < p2:
                return -1
        return 0
        