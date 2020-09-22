# 421. Maximum XOR of Two Numbers in an Array

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
#         dmax = 0
#         for i in range(len(nums)-1):
#             for j in range(i+1,len(nums)):
#                 dmax = max(dmax, nums[i]^nums[j])
#                 # print(i,j,nums[i]^nums[j])
#         return dmax
        
        res = 0
        for i in range(31,-1,-1):
            res <<= 1
            pre = {n>>i for n in nums}
            res += any(res^1^p in pre for p in pre)
        return res

#         # Compute length L of max number in a binary representation
#         L = len(bin(max(nums))) - 2
#         # zero left-padding to ensure L bits for each number
#         nums = [[(x >> i) & 1 for i in range(L)][::-1] for x in nums]
        
#         max_xor = 0
#         trie = {}
#         for num in nums:
#             node = trie
#             xor_node = trie
#             curr_xor = 0
#             for bit in num:
#                 # insert new number in trie
#                 if not bit in node:
#                     node[bit] = {}
#                 node = node[bit]
                
#                 # to compute max xor of that new number 
#                 # with all previously inserted
#                 toggled_bit = 1 - bit
#                 if toggled_bit in xor_node:
#                     curr_xor = (curr_xor << 1) | 1
#                     xor_node = xor_node[toggled_bit]
#                 else:
#                     curr_xor = curr_xor << 1
#                     xor_node = xor_node[bit]
                    
#             max_xor = max(max_xor, curr_xor)

#         return max_xor