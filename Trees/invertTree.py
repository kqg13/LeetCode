# Easy tree problem 226: Invert Binary Tree

# This problem was inspired by Max Howell, founder of Homebrew from his tweet:
# Google: 90% of our engineers use the software you wrote (Homebrew), but
# you can’t invert a binary tree on a whiteboard so f*** off.


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
    def invertTree(self, root):
        """
        :param root: TreeNode
        :return: TreeNode
        """
        if not root:
            return None
        right = self.invertTree(root.right)
        left = self.invertTree(root.left)
        root.left = right
        root.right = left
        return root


# Test
s = Solution()
r = TreeNode(4)
r.left = TreeNode(2)
r.left.left = TreeNode(1)
r.left.right = TreeNode(3)
r.right = TreeNode(7)
print(s.invertTree(r))
