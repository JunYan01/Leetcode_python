# 1032. Stream of Characters


class StreamChecker:
    

    def __init__(self, words: List[str]):
        self.trie = {}
        self.stream = deque([])
        # self.stream = []
        for word in set(words):
            node = self.trie       
            for ch in word[::-1]:
                if not ch in node:
                    node[ch] = {}
                node = node[ch]
            node['$'] = word
        
        
    def query(self, letter: str) -> bool:
        self.stream.appendleft(letter)
        # self.stream.insert(0,letter)
        node = self.trie
        for ch in self.stream:
            # 见好就收, self.trie（node）里已经有符合要求的
            if '$' in node:
                return True
            # 如果不match, 之前的必定也没有符合要求的
            if not ch in node:
                return False
            # 如果match此前的，必须继续走完检测
            node = node[ch]
        # 如果self.stream走完，self.trie(node) 里还没有走完，就不对了
        return '$' in node

#     def __init__(self, words: List[str]):
#         self.suffixTree = {}
        
#         for word in set(words):
#             node = self.suffixTree
#             for ch in word[::-1]:
#                 if not ch in node:
#                     node[ch] = {}
#                 node = node[ch]
#             node['$'] = True
#             # print(word,self.suffixTree)
#         self.queries = []
#         # print(self.suffixTree)
            
#         # print(self.letters)
#         return 

#     def query(self, letter: str) -> bool:
#         self.queries.append(letter)
#         node = self.suffixTree
#         # word = self.queries[::]
#         # # print(''.join(self.queries))
#         # while len(word)>0:
#         #     ch = word.pop()
#         for ch in self.queries[::-1]:
#             # print(ch)
#             if '$' in node:
#                 return True
#             if not ch in node:
#                 return False
#             else:
#                 node = node[ch]
            
#         # print(letter,''.join(self.queries),node,'$' in node)
#         return '$' in node
        
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)