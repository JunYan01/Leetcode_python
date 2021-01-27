1437  Check If All 1's Are at Least Length K Places Away


class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return True
        for i, d in enumerate(nums):
            # print(i, d)
            if d == 1:
                try:
                    # print(i - p - 1)
                    if i - p - 1 < k  :
                        return False
                except:
                    # print(i)
                    pass
                p = i
        return True