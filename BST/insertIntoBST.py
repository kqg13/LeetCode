# 701: Insert into a Binary Search Tree
# Definition for a binary tree node.
# https://leetcode.com/problems/insert-into-a-binary-search-tree/


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        self.insertIntoBSThelper(root, val)
        return root

    def insertIntoBSThelper(self, node, val):
        if node is None:
            return TreeNode(val)
        if val > node.val:
            node.right = self.insertIntoBSThelper(node.right, val)
        if val < node.val:
            node.left = self.insertIntoBSThelper(node.left, val)
        return node


s = Solution()
t = TreeNode(4)
t.left = TreeNode(2)
t.right = TreeNode(7)
t.left.left = TreeNode(1)
t.right.left = TreeNode(3)
s.insertIntoBST(t, 5)

