11Container With Most Water

class Solution:
    def maxArea(self, height: List[int]) -> int:
        
#         i, j = 0, len(height)-1
#         maxValue = min(height[i],height[j])*(j-i)
#         while i < j:
#             if height[i] < height[j]:
#                 i += 1
#             else:
#                 j -= 1
#             maxValue =  max(min(height[i],height[j])*(j-i),maxValue)
                
            
#         return maxValue
        ans, l, r = 0, 0, len(height) - 1
        while l < r:
            # ans = max(min(height[l],height[r])*(r-l),ans)
            if height[l] < height[r]:
                ans = max(height[l]*(r-l),ans)
                l += 1
            else:
                ans = max(height[r]*(r-l),ans)
                r -= 1
        return ans