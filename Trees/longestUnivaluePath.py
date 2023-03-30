# Easy tree/recursion problem 687: Longest Univalue Path

# Given a binary tree, find the length of the longest path where each node in
# the path has the same value. This path may or may not pass through the root.
#
# Note: The length of path between two nodes is represented by the number of
# edges between them.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxpath = 0

        def univaluepath_rec(root):
            if not root:
                return 0

            leftpath = univaluepath_rec(root.left)
            rightpath = univaluepath_rec(root.right)

            if root.left and root.val == root.left.val:
                leftpath += 1
            else:
                leftpath = 0

            if root.right and root.val == root.right.val:
                rightpath += 1
            else:
                rightpath = 0

            self.maxpath = max(self.maxpath, leftpath + rightpath)
            return max(leftpath, rightpath)

        univaluepath_rec(root)
        return self.maxpath
