# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        self.currentClose = float("inf")
        self.distance = float("inf")

        def traverse(node, target):
            if node==None: return
            distance = abs(node.val-target)
            if distance<self.distance:
                self.distance = distance
                self.currentClose = node.val
            elif distance==self.distance:
                self.currentClose = min(node.val, self.currentClose)

            if target==node.val:
                return
            if target<node.val:
                traverse(node.left, target)
            else:
                traverse(node.right, target)
        traverse(root, target)
        return self.currentClose