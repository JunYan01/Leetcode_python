820Short Encoding of Words

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
#         self.root = {}
#         self.end_of_word = '#'
        
#         def insert( word):
#             node = self.root
#             for char in word:
#                 node = node.setdefault(char, {})
#             node[self.end_of_word] = self.end_of_word
        
#         for word in words:
#             insert(word[::-1])
        
#         print(self.root)
        
#         return 0
        s = set(words)
        # print(s)
        for word in words:
            # print(word)
            for i in range(len(word)-1,0,-1):
                if word[i:] in s:
                    # print(word[i:])
                    s.remove(word[i:])
                # try:
                #     s.remove(word[i:])
                # except:
                #     continue
            # print(s)
        ans = 0
        # print(s)
        for w in s:
            ans += len(w) + 1
        return ans
        