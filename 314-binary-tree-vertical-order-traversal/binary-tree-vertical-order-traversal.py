# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
(level, column, value)

"""
from collections import deque

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root==None: return []
        columnMap = defaultdict(list)
        q = deque()
        q.append((0, root))
        while q:
            column, node = q.popleft()
            columnMap[column].append(node.val)
            if node.left!=None:
                q.append((column-1, node.left))
            if node.right!=None:
                q.append((column+1, node.right))
        
        minKey = min(columnMap.keys())
        maxKey = max(columnMap.keys())
        result = []
        for i in range(minKey, maxKey+1, 1):
            result.append(columnMap[i])
        return result

        