# 1325: Delete Leaves With a Given Value
# https://leetcode.com/problems/delete-leaves-with-a-given-value/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Post-order traversal
    def removeLeafNodes(self, root, target):
        if root:
            root.left = self.removeLeafNodes(root.left, target)
            root.right = self.removeLeafNodes(root.right, target)
            if root.left is None and root.right is None and root.val == target:
                return None
        return root


s = Solution()
