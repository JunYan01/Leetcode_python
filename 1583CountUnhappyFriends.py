# 1583. Count Unhappy Friends

class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        better = {}
        for i,j in pairs:
            better[i] = preferences[i][0:preferences[i].index(j)]
            better[j] = preferences[j][0:preferences[j].index(i)]
        # print(better)
        count = 0
        for i,arr in better.items():
            # print(i,arr)
            for j in arr:
                if i in better[j]:
                    count += 1
                    break
        return count