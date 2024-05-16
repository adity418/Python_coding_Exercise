# Height of Binary Tree(Max Depth)

class Node:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root):
        if root == None:
            return 0
        else:
            ldepth = self.maxDepth(root.left)
            rdepth = self.maxDepth(root.right)

            if ldepth > rdepth:
                return(1+ldepth)
            else:
                return(1+rdepth)