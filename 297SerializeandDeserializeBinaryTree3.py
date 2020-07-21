# 297. Serialize and Deserialize Binary Tree
# BFS层级遍历
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
        
        string = self.traverse(root)
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
        if len(data) == 0:
            return None
        
        data = [s for s in data.split(',')]
        # print(data)
        return self.dsp(data)
    
    def dsp(self,data):
        if len(data) == 0:
            return None
        
        val = data.pop(0)
        
        # print(val)
        if val == '#':
            return None
        # print(val)
        node = TreeNode(int(val))
        queue = [node]
        while len(queue) > 0:
            curr = queue.pop(0)
            # print(curr)
            if curr.val == '#':
                continue
            left = data.pop(0)
            if left == '#':
                curr.left =None
            else:
                curr.left = TreeNode(int(left))
                queue.append(curr.left)
                
            right = data.pop(0)
            if right == '#':
                curr.right = None
            else:
                curr.right = TreeNode(int(right))
                queue.append(curr.right)
        
        return node
        
        
        
        
        
    def traverse(self,root):
        if root == None:
            # string.append('#') 
            # print(string)
            return []
        
        queue = [root]
        string = []
        # print(queue)
        while len(queue) >0:
            curr = queue.pop(0)
            # print(curr)
            
            if not curr:
                string.append('#')
                continue
            string.append(str(curr.val))
            queue.append(curr.left)
            queue.append(curr.right)
        
        # print(string)
        return string
        
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))