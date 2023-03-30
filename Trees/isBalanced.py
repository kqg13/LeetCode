# Easy Tree Problem 110: Balanced Binary Tree

# Given a binary tree, determine if it is height-balanced.
# For this problem, a height-balanced binary tree is defined as:
# a binary tree in which the left and right subtrees of every node differ in
# height by no more than 1.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        rep = str(self.val)
        return rep


class Solution:
    def isBalanced(self, root):
        return self.isBalancedHelper(root)[1]

    def isBalancedHelper(self, root):
        if root is None:
            return (0, True)
        hl, bl = self.isBalancedHelper(root.left)
        hr, br = self.isBalancedHelper(root.right)
        h = -1
        b = bl and br
        if b and abs(hl - hr) <= 1:
            h = max(hl, hr) + 1
        else:
            b = False
        return (h, b)


t = TreeNode(1)
t.left = TreeNode(2)
t.right = TreeNode(2)
t.left.left = TreeNode(3)
t.left.right = TreeNode(3)
t.left.left.left = TreeNode(4)
t.left.left.right = TreeNode(4)

s = Solution()
print(s.isBalanced(t))
