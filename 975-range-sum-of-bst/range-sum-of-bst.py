# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if root==None: return 0
        if low<=root.val<=high:
            left = self.rangeSumBST(root.left, low, high)
            right = self.rangeSumBST(root.right, low, high)
            return root.val+left+right
        elif high<root.val:
            return self.rangeSumBST(root.left, low, high)
        else:
            return self.rangeSumBST(root.right, low, high)
        