# Definition for a binary tree node.
import math
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        iter_node = root
        path = []
        path.append(iter_node)
        end_node = root
        if root == None:
            return res
        while path:
            while iter_node.left != None: # find the left node
                path.append(iter_node)
                iter_node = iter_node.left
            res.append(iter_node.val) #
            if iter_node.right: # if it is a parent node
                iter_node = iter_node.right
            else:               # if it is a leaf node
                iter_node = path.pop()
                iter_node.left = None # cut
        return res


def deserialize(string):
    if string == '{}':
        return None
    nodes = [None if val == 'null' else TreeNode(int(val))
             for val in string.strip('[]{}').split(',')]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left  = kids.pop()
            if kids: node.right = kids.pop()
    return root


test = Solution()
node = deserialize('[2,3,null,1]')
print test.inorderTraversal(node)

