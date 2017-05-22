# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    flag = True
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if (p == None and q != None) or (p != None and q == None):
            self.flag = False
        elif p == None and q == None:
            return True
        elif p.val != q.val:
            self.flag = False
        else:
            self.isSameTree(p.left, q.left)
            self.isSameTree(p.right, q.right)
        return self.flag

node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)

node1.left = node2
node1.right = node3

node4 = TreeNode(1)
node5 = TreeNode(2)
node6 = TreeNode(3)

node4.left = node5
# node4.right = node6

test = Solution()
print test.isSameTree(node1 ,node4)
