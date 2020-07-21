# 297. Serialize and Deserialize Binary Tree
# 后序
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
        
        val = data.pop()
        # print(data)
        # print(val)
        if val == '#':
            return None
        node = TreeNode(val)
        
        node.right = self.dsp(data)
        node.left = self.dsp(data)
        
        return node
        
        
        
        
        
    def traverse(self,root,string):
        if root == None:
            string.append('#') 
            # print(string)
            return
        
       
        self.traverse(root.left,string)
        self.traverse(root.right,string)
        string.append(str(root.val))
        # print(string)
        
        return
        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))