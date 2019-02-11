# A well-known Medium tree problem #98: Validate Binary Search Tree

# Given a binary tree, determine if it is a valid binary search tree (BST).


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x=None):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: 'TreeNode') -> 'bool':

        def bst_helper(root, lower, upper):
            if root is None:
                return True
            if root.val >= upper or root.val <= lower:
                return False
            return bst_helper(root.left, lower, root.val) and bst_helper(root.right, root.val, upper)

        return bst_helper(root, float('-inf'), float('inf'))


# Test
s = Solution()
r = TreeNode(10)
r.left = TreeNode(8)
r.left.left = TreeNode(7)
r.left.right = TreeNode(9)
r.right = TreeNode(15)
r.right.left = TreeNode(13)
r.right.right = TreeNode(16)
print(s.isValidBST(r))
