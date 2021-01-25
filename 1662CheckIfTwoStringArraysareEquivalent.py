1662. Check If Two String Arrays are Equivalent

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        # print(''.join(word1))
        # print(''.join(word2))
        return ''.join(word1) == ''.join(word2)