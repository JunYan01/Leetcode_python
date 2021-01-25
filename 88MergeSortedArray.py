88  Merge Sorted Array

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j = m - 1, n - 1
        while i >= 0 and j >= 0:
            if nums1[i] >= nums2[j]:
                nums1[i+j+1] = nums1[i]
                i -= 1
            else:
                nums1[i+j+1] = nums2[j]
                j -= 1
            
        if i < 0:
            nums1[0:j+1] = nums2[0:j+1]
            
        return
        # nums1[m:m+n] = nums2
        # nums1.sort()
        
            
        return
            