# 211. Add and Search Word 


class TrieNode:
    # Initialize your data structure here.
    def __init__(self):
        self.word=False
        self.children={}


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        node = self.root
        for i in word:
            if i not in node.children:
                node.children[i] = TrieNode()
            node = node.children[i]
        node.word = True
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        # node = self.root
        def searchHelper(word: str, node: TrieNode) -> bool:
        # print(word)
            
            for i,ch in enumerate(word):
                # print(ch)
                if ch not in node.children:
                    if ch == '.':
                        for x in node.children:
                            if searchHelper(word[i+1:],node.children[x]):
                                return True
                    return False
                else:
                    node = node.children[ch]
            return node.word
        
        return searchHelper(word, self.root)
        # x = searchHelper(word, node)
        # print('result for '+ word+' is ' + str(x))
        # return x
     
                
#         if word == '.':
#             if node.children:
#                 # print('(node.children',node.children)
#                 return any([node.children[i].word for i in node.children])
#             return False
        
#         l = word[0]
#         if l == '.':
#             if not node.children:
#                 return False
#             return any([self.searchHelper(word[1:],node.children[n]) for n in node.children])
#         else:
#             if l not in node.children:
#                 return False
#             if l == word:
#                 return node.children[l].word
#             return self.searchHelper(word[1:],node.children[l])

# class WordDictionary:

#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.trie = {}
        

#     def addWord(self, word: str) -> None:
#         """
#         Adds a word into the data structure.
#         """
#         node = self.trie
        
#         for ch in word:
#             if not ch in node:
#                 node[ch] = {}
#             node = node[ch]
#         node['$'] = True
        
#     def search(self, word: str) -> bool:
#         """
#         Returns if the word is in the data structure. A word could contain the dot character '.' to represent any letter.
#         """
#         def search_in_node(word, node) -> bool:
#             for i, ch in enumerate(word):
#                 if not ch in node:
#                     # if the current character is '.'
#                     # check all possible nodes at this level
#                     if ch == '.':
#                         for x in node:
#                             if x != '$' and search_in_node(word[i + 1:], node[x]):
#                                 return True
#                     # if no nodes lead to answer
#                     # or the current character != '.'
#                     return False
#                 # if the character is found
#                 # go down to the next level in trie
#                 else:
#                     node = node[ch]
#             return '$' in node
        
#         return search_in_node(word, self.trie)
            
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)