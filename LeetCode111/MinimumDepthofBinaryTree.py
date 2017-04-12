path = []
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def deserialize(string):
    if string == '[]':
        return None
    nodes = [None if val == 'null' else TreeNode(int(val))
             for val in string.strip('[]{}').split(',')]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left = kids.pop()
            if kids: node.right = kids.pop()
    return root

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        if root.left is None:
            return self.treeDepth(root.right)+1
        if root.right is None:
            return self.treeDepth(root.left)+1
        hl = self.treeDepth(root.left)
        hr = self.treeDepth(root.right)
        print hr
        return min(hl, hr)+1



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
            # h = max(hl, hr)
            if hr == 0 or hl == 0:
                return hr+hl+1
            else:
                return min(hl,hr)+1
        else:return 0


tree = deserialize('[-9,-3,2,null,4,4,0,-6,null,-5]')
test = Solution()
print test.minDepth(tree)
# print test.treeShortestPath(tree)