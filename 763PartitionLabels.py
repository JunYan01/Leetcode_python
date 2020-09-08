# 763. Partition Labels

class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last = {c: i for i, c in enumerate(S)}
        pre = curr = 0
        res = []
        for i, c in enumerate(S):
            curr = max(curr, last[c])
            if i == curr:
                res.append(i - pre + 1)
                pre = i + 1
            
        return res