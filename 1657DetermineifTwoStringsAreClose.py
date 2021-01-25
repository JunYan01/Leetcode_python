1657Determine if Two Strings Are Close

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        dic1 = {}
        dic2 = {}
        for w in word1:
            dic1[w] = dic1.get(w,0) + 1 
        for w in word2:
            if w not in word1:
                return False
            dic2[w] = dic2.get(w,0) + 1 
        # print(sorted(list(dic1.values())))
        # print(sorted(list(dic2.values())))
        dic1 = sorted(list(dic1.values()))
        dic2 = sorted(list(dic2.values()))
        return dic1 == dic2