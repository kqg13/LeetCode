# Easy binary search tree problem 270: Closest Binary Search Tree

# Given a non-empty binary search tree and a target value, find the value in
# the BST that is closest to the target.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        rval = root.val
        while root:
            rdelta = abs(root.val - target)
            if rdelta < rval - target:
                rval = rdelta
            else:
                root = root.left if root.val > target else root.right
        return rval

    def closestValueRecursive(self, root, target):
        self.rval = float('inf')

        def helper(root, target):
            if root:
                delta = abs(root.val - target)
                if delta < abs(self.rval - target):
                    self.rval = root.val

                helper(root.left, target) if root.val > target else\
                    helper(root.right, target)

            return self.rval

        return helper(root, target)

