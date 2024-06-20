# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
   1.   
  2  3

node1 = (node1,prev=0)
left+right
node2 = (node2, prev=10 = 10*(0+1)) return prev+curVal
"""

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        

        def dfs(curNode, prev):
            if curNode==None: return 0
            if curNode.left==None and curNode.right==None:
                return prev+curNode.val
            nextPrev = 10*(prev+curNode.val)
            left = dfs(curNode.left, nextPrev)
            right = dfs(curNode.right, nextPrev)
            return left+right
        return dfs(root, 0)