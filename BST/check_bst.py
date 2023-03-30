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
        if root is None: return True
        isBST = self.isValidBSTHelper(root, float('-inf'), float('inf'))
        return isBST

    def isValidBSTHelper(self, node, lower, upper):
        if node is None:
            return True
        if node.val <= lower or node.val >= upper:
            return False
        else:
            isRightBST = self.isValidBSTHelper(node.right, node.val, upper)
            isLeftBST = self.isValidBSTHelper(node.left, lower, node.val)
            return isRightBST and isLeftBST


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
