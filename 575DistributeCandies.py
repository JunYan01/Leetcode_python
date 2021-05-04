575  Distribute Candies

class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        # dic = {}
        # n = len(candyType)
        # for i in candyType:
        #     dic[i] = dic.get(i,0) + 1
        # if len(dic)<n//2:
        #     return len(dic)
        # else:
        #     return n//2
        


#                     
#                 count += 1

        dic = {}
        n = len(candyType)
        count = 0
        for i in candyType:
            if i not in dic:
                count += 1
            dic[i] = 1
        if count<n//2:
            return count
        else:
            return n//2



