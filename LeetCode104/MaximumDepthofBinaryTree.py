# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        hl = self.treeDepth(root.left)
        hr = self.treeDepth(root.right)
        return max(hl, hr)+1



    def treeDepth(self,tree):
        """
        :type tree: TreeNode
        :rtype: int
        """
        hl = 0
        hr = 0
        h = 0
        if tree != None:
            hl = self.treeDepth(tree.left)
            hr = self.treeDepth(tree.right)
            h = max(hl, hr)
            return h+1
        else:return 0

