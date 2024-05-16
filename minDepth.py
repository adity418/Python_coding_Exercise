# Min Depth of Binary Tree

class Node:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None
    
class Solution:
    def minDepth(self, root):
        if root == None:
            return 0
        else:
            ldepth = self.minDepth(root.left)
            rdepth = self.minDepth(root.right)

            if ldepth > rdepth:
                return 1+rdepth
            else:
                return 1+ldepth