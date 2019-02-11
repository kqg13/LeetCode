# Easy BST problem 700: Search in a Binary Search Tree

# Given the root node of a binary search tree (BST) and a value.
# You need to find the node in the BST that the node's value equals the
# given value. Return the subtree rooted with that node. If such node doesn't
# exist, you should return NULL.
#
# Note that an empty tree is represented by # NULL, therefore you would see
# the expected output (serialized tree format) as [], not null.


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
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root:
            rval = root.val
            if rval > val:
                return self.searchBST(root.left, val)
            elif rval < val:
                return self.searchBST(root.right, val)
            else:
                return root
        return []


# Test
r = TreeNode(4)
r.left = TreeNode(2)
r.left.left = TreeNode(1)
r.left.right = TreeNode(3)
r.right = TreeNode(7)
