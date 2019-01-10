# Easy Problem 104: Max depth of a binary tree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return max(self.maxDepth(root.left), self.maxDepth(root.right))+1 if root else 0


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
sol = Solution()
print(sol.maxDepth(root))


# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):

    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if root is None:
            return 0
        maxval = 1
        for child in root.children:
            depthcount = self.maxDepth(child) + 1
            maxval = max(maxval, depthcount)
        return maxval
