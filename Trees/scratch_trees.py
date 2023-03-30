# Easy Problem 965: Univalued binary tree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        the_val = root.val
        return self.isUnivalTreeHelper(root, the_val)

    def isUnivalTreeHelper(self, node, the_val):
        if node is None:
            return True
        if node.val != the_val:
            return False
        return  node.val == the_val and \
                self.isUnivalTreeHelper(node.left, the_val) and \
                self.isUnivalTreeHelper(node.right, the_val)


root = TreeNode(1)
root.left = TreeNode(1)
root.right = TreeNode(1)
root.left.left = TreeNode(1)
root.left.right = TreeNode(0)
root.right.left = TreeNode(1)
sol = Solution()
print(sol.isUnivalTree(root))
