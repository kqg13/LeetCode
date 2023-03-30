# 671: Second Minimum Node In a Binary Tree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        self.node_set = set()
        self.postOrderCollect(root)
        print(self.node_set)

    def postOrderCollect(self, node):
        if node:
            self.postOrderCollect(node.left)
            self.postOrderCollect(node.right)
            self.node_set.add(node.val)


s = Solution()
target = 9
t = TreeNode(5)
t.left = TreeNode(3)
t.right = TreeNode(6)
t.left.left = TreeNode(2)
t.left.right = TreeNode(4)
t.right.right = TreeNode(7)
s.findTarget(t, target)
