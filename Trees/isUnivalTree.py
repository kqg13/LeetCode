# Easy Problem 965: Univalued binary tree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.node_vals = []

    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        if root:
            self.node_vals.append(root.val)
            self.isUnivalTree(root.left)
            self.isUnivalTree(root.right)
        return len(set(self.node_vals)) == 1


root = TreeNode(1)
root.left = TreeNode(0)
root.right = TreeNode(1)
root.left.left = TreeNode(1)
root.left.right = TreeNode(1)
root.right.left = TreeNode(1)
sol = Solution()
print(sol.isUnivalTree(root))
print(sol.node_vals)
