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
        # def _change_links(node):
        #     if node:
        #         _change_links(node.left)
        #         _change_links(node.right)
        #         if node.left and node.right:
        #             temp = TreeNode(node.left)
        #             node.left = node.right
        #             node.right = temp
        #             self.new_tree = node
        #         elif node.left and not node.right:
        #             node.right = node.left
        #             node.left = None
        #             self.new_tree = node
        #         elif node.right and not node.left:
        #             node.left = node.right
        #             node.right = None
        #             self.new_tree = None
        #
        # self.ans = self.new_tree = TreeNode(root.val)
        # _change_links(root)
        # return self.ans


# Test
s = Solution()
r = TreeNode(4)
r.left = TreeNode(2)
r.left.left = TreeNode(1)
r.left.right = TreeNode(3)
r.right = TreeNode(7)
print(s.invertTree(r))
print(4589.16 - 2040.46)