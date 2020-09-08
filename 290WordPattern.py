# 290. Word Pattern

class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:        
        str = str.split(' ')
        if len(pattern) != len(str):return False
        cache, cache2 = {}, {}
        for i,word in zip(pattern,str):
            # print(i,word)
            if i in cache and cache[i] != word:
                return False
            else:
                cache[i] = word
            if word in cache2 and cache2[word] != i:
                return False
            else:
                cache2[word] = i
                
        # print(cache)
        # print(cache2)
        return True