# 229. Majority Element II


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # arr = defaultdict(int)
        # k = len(nums)//3+1
        # for n in nums:
        #     arr[n] += 1
        # res = []
        # for a in arr:
        #     if arr[a] >= k:
        #         res.append(a)
        # return res
        
        # arr = {}
        # k = len(nums)//3+1
        # for n in nums:
        #     arr[n] = arr.get(n,0)+1
        # res = []
        # for a in arr:
        #     if arr[a] >= k:
        #         res.append(a)
        # return res
        
        if not nums:
            return []
        count1, count2, candidate1, candidate2 = 0, 0, None, None
        for n in nums:
            if candidate1 == n:
                count1 += 1
            elif candidate2 == n:
                count2 += 1
            elif count1 == 0:
                candidate1 = n
                count1 = 1
            elif count2 == 0:
                candidate2 = n
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
        
        res = []
        for n in [candidate1, candidate2]:
            if nums.count(n) > len(nums)//3:
                res.append(n)
        return res