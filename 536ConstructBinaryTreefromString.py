536  Construct Binary Tree from String

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def str2tree(self, s: str) -> TreeNode:
#         string = ''
#         # queue = [TreeNode(0),'(']
#         queue = []
#         for w in s:
#             if w == '-':
#                 string = w
#                 continue
#             if w == '(' or w == ')' :
#                 if string:
#                     print(int(string))
                    
#                     node = TreeNode(int(string))
#                     # x = queue.pop()
#                     # if x == '(':
#                     #     queue[-1].left = node
#                     # if x == ')':
#                     #     queue[-1].left = node
#                     queue.append(node.val)
#                 queue.append(w)
#                 string = ''
#                 continue
#             string += w
#         print(queue)
#         return None
        if len(s) == 0: return None
        st = []
        i = 0
        while i<len(s):
            j = i
            if s[i] == ')':
                st.pop()
            elif (s[i] >= '0' and s[i] <= '9') or s[i] == '-':
                while i + 1<len(s) and s[i+1] >= '0' and s[i+1] <= '9':
                    i += 1
                # print(j,i,i+1,s[j:i+1])
                cur = TreeNode(int(s[j:i+1]))
                if len(st):
                    t = st[-1]
                    if not t.left:
                        t.left = cur
                    else:
                        t.right = cur
                st.append(cur)
            
            # print([x.val for x in st])
            i += 1
        return st[-1]
        