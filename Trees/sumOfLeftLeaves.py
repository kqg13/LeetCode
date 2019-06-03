# Easy tree problem 404: Sum of Left Leaves

# Find the sum of all left leaves in a given binary tree

#    3
#   / \
#  9  20
#    /  \
#   15   7
# Output: 24


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sumOfLeftHelper(self, node, direction):
        if node is None:
            return 0
        if node.left is None and node.right is None and direction is True:
            self.sum_lefts += node.val
        self.sumOfLeftHelper(node.left, True)
        self.sumOfLeftHelper(node.right, False)

    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        self.sum_lefts = 0
        self.sumOfLeftHelper(root, False)
        return self.sum_lefts


s = Solution()
t = TreeNode(3)
t.left = TreeNode(9)
t.right = TreeNode(20)
t.right.left = TreeNode(15)
t.right.right = TreeNode(7)
print(s.sumOfLeftLeaves(t))
