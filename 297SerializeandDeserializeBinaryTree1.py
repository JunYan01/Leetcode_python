# 297. Serialize and Deserialize Binary Tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        string = []
        self.traverse(root,string)
        # print(string)
        string = ','.join(string)
        # print(string)
        return string
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        # print(data)
        data = [s for s in data.split(',')]
        # print(data)
        return self.dsp(data)
    
    def dsp(self,data):
        if not data:
            return None
        
        val = data.pop(0)
        # print(data)
        # print(val)
        if val == '#':
            return None
        node = TreeNode(val)
        node.left = self.dsp(data)
        node.right = self.dsp(data)
        
        return node
        
        
        
        
        
    def traverse(self,root,string):
        if root == None:
            string.append('#') 
            # print(string)
            return
        
        string.append(str(root.val))
        # print(string)
        self.traverse(root.left,string)
        self.traverse(root.right,string)
        
        return
        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))