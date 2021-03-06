# 208. Implement Trie (Prefix Tree)

# class TrieNode:
#         # Initialize your data structure here.
#         def __init__(self):
#             self.word=False
#             self.children={}

# class Trie:

#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.root = TrieNode()

        

#     def insert(self, word: str) -> None:
#         """
#         Inserts a word into the trie.
#         """
#         node = self.root
#         for i in word:
#             if i not in node.children:
#                 node.children[i] = TrieNode()
#             node = node.children[i]
#         node.word = True
            
        

#     def search(self, word: str) -> bool:
#         """
#         Returns if the word is in the trie.
#         """
#         node = self.root
#         for i in word:
#             if i not in node.children:
#                 return False
#             node = node.children[i]
#         return node.word
        

#     def startsWith(self, prefix: str) -> bool:
#         """
#         Returns if there is any word in the trie that starts with the given prefix.
#         """
#         node = self.root
#         for i in prefix:
#             if i not in node.children:
#                 return False
#             node = node.children[i]
#         return True
        
    


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}

    def insert(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        node = self.trie
        
        for ch in word:
            if not ch in node:
                node[ch] = {}
            node = node[ch]
        node['$'] = True
            
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        def search_in_node(word, node) -> bool:
            for ch in word:
                if not ch in node:
                    return False
                # if the character is found
                # go down to the next level in trie
                else:
                    node = node[ch]
            return '$' in node
        
        return search_in_node(word, self.trie)
        
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.trie
        for ch in prefix:
            if not ch in node:
                return False
            # if the character is found
            # go down to the next level in trie
            else:
                node = node[ch]
        return True
    

        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)