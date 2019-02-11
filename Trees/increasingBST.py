# Easy tree problem 897: Increasing Order Search Tree

# Given a tree, rearrange the tree in in-order so that the leftmost node in the
# tree is now the root of the tree, and every node has no left child and only
# 1 right child.


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

    def increasingBST(self, root):
        """
        :param root: TreeNode
        :return: TreeNode
        """

        self.ans = self.new_tree = TreeNode(None)

        def _inorder(node):
            if node:
                _inorder(node.left)
                node.left = None
                self.new_tree.right = node
                self.new_tree = node
                _inorder(node.right)

        _inorder(root)
        return self.ans.right


# Test
s = Solution()
r = TreeNode(4)
r.left = TreeNode(2)
r.left.left = TreeNode(1)
r.left.right = TreeNode(3)
r.right = TreeNode(7)
print(s.increasingBST(r))
