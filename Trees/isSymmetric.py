# Easy Problem 101: Symmetric Tree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def isSymmetric(self, root):
        """
        :type p: TreeNode
        :rtype: bool
        """
        return self.is_mirror(root, root)

    def is_mirror(self, ltree, rtree):
        """ For two trees to be mirror images, 3 conditions must be true:
            1 - Their root value must be same
            2 - left subtree of ltree & right subtree of rtree must be mirrors
            3 - right subtree of ltree & left subtree of rtree must be mirrors
        """
        if ltree is None and rtree is None:
            return True
        if ltree is None or rtree is None:
            return False
        if ltree is not None and rtree is not None:
            return (ltree.val == rtree.val) and \
                   self.is_mirror(ltree.left, rtree.right) and \
                   self.is_mirror(ltree.right, rtree.left)


root = TreeNode(1)
root.left = TreeNode(2)
root.left.right = TreeNode(3)
root.right = TreeNode(2)
root.right.right = TreeNode(3)

sol = Solution()
print(sol.isSymmetric(root))
