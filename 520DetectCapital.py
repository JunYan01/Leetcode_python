# 520. Detect Capital 

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        n = len(word)
        if  n <= 1:
            return True
        if word[0].islower() == True:
            return all([x.islower() for x in word[1:]])
        return all([x.islower() for x in word[1:]]) or all([x.isupper() for x in word[1:]])

        