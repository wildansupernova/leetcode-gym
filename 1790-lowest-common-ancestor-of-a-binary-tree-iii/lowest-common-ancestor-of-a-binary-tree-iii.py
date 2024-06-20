"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

5 -> Node5
1 -> Node1
3 -> Node3

p = Node3
q = Node3

"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        a = p 
        b = q
        while a!=b:
            a = q if a == None else a.parent
            b = p if b == None else b.parent
        return a
            