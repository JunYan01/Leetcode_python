# 404. Sum of Left Leaves


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        
#         This method avoid base case assign, which is not good style
#         def recursive(node, summary) -> int:
#             # if not node:
#             #     return summary
            
#             if node.left:
#                 if not node.left.left and not node.left.right:
#                     summary += node.left.val
#                 summary = recursive(node.left,summary)
#             if node.right:
#                 summary = recursive(node.right,summary)
#             return summary
        
#         return recursive(root,0) if root else 0


#           Just a little better
#         def recursive(node, summary) -> int:
#             if not node:
#                 return summary          
            
#             if node.left:
#                 if not node.left.left and not node.left.right:
#                     summary += node.left.val
#                 summary = recursive(node.left,summary)
#             if node.right:
#                 summary = recursive(node.right,summary)
#             return summary
        
#         return recursive(root,0)


#         def recursive(node) -> int:
#             if not node:
#                 return 0
#             sum = 0
#             if node.left:
#                 if not node.left.left and not node.left.right:
#                     sum += node.left.val
#                 else:
#                     sum += recursive(node.left)
#             if node.right:
#                 sum += recursive(node.right)
            
#             return sum
        
#         return recursive(root)

#         def recursive(node) -> int:
#             if not node:
#                 return 0
#             num = 0
#             # try:
#             #     if not node.left.left and not node.left.right:
#             #         num += node.left.val
#             # except:
#             #     pass
#             if node.left and not node.left.left and not node.left.right:
#                 num += node.left.val
#             num += recursive(node.left)
#             num += recursive(node.right)
#             return num
        
#         return recursive(root)

        # If DFS, quickest I have tried !!!
#         if not root:
#             return 0

#         stack = deque([root])
#         sum = 0
#         while stack:
#             node = stack.pop()
#             if node.left and not node.left.left and not node.left.right:
#                 sum += node.left.val
#             if node.right:
#                 stack.append(node.right)
#             if node.left:
#                 stack.append(node.left)
#         return sum

         
        total_sum = 0
        current_node = root
        while current_node is not None:
            # If there is no left child, we can simply explore the right subtree
            # without needing to worry about keeping track of currentNode's other
            # child.
            if current_node.left is None: 
                current_node = current_node.right 
            else: 
                previous = current_node.left 
                # Check if this left node is a leaf node.
                if previous.left is None and previous.right is None:
                    total_sum += previous.val
                # Find the inorder predecessor for currentNode.
                while previous.right is not None and previous.right is not current_node:
                    previous = previous.right
                # We've not yet visited the inorder predecessor. This means that we 
                # still need to explore currentNode's left subtree. Before doing this,
                # we will put a link back so that we can get back to the right subtree
                # when we need to.
                if previous.right is None:
                    previous.right = current_node  
                    current_node = current_node.left  
                # We have already visited the inorder predecessor. This means that we
                # need to remove the link we added, and then move onto the right
                # subtree and explore it.
                else:
                    previous.right = None
                    current_node = current_node.right
        return total_sum
                
            