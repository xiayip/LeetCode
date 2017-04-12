# Definition for a binary tree node.
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
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        hr = self.treeDepth(root.left)
        hl = self.treeDepth(root.right)
        print hr,hl
        if abs(hl-hr)>1:
            return False
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)

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
            h = max(hl,hr)
            return h+1
        return 0




testTree = deserialize('[1,2,2,3,null,null,3,4,null,null,4]')
test = Solution()
print test.isBalanced(testTree)

def drawtree(root):
    def height(root):
        return 1 + max(height(root.left), height(root.right)) if root else -1
    def jumpto(x, y):
        t.penup()
        t.goto(x, y)
        t.pendown()
    def draw(node, x, y, dx):
        if node:
            t.goto(x, y)
            jumpto(x, y-20)
            t.write(node.val, align='center', font=('Arial', 12, 'normal'))
            draw(node.left, x-dx, y-60, dx/2)
            jumpto(x, y-20)
            draw(node.right, x+dx, y-60, dx/2)
    import turtle
    t = turtle.Turtle()
    t.speed(0); turtle.delay(0)
    h = height(root)
    jumpto(0, 30*h)
    draw(root, 0, 30*h, 40*h)
    t.hideturtle()
    turtle.mainloop()

# if __name__ == '__main__':
#     drawtree(deserialize('[1,2,3,null,1]'))