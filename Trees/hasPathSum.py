# Easy tree problem 112: Path Sum
# https://leetcode.com/problems/path-sum/

# Given a binary tree and a sum, determine if the tree has a root-to-leaf path
# such that adding up all the values along the path equals the given sum.


# Example: Given the below binary tree and sum = 22, return true, as there exist
# a root-to-leaf path 5->4->11->2 which sum is 22.

#       5
#      / \
#     4   8
#    /   / \
#   11  13  4
#  /  \      \
# 7    2      1

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None:
            return False

        sum -= root.val

        if root.left is None and root.right is None:
            return sum == 0

        l = self.hasPathSum(root.left, sum)
        r = self.hasPathSum(root.right, sum)
        return l or r


t = TreeNode(5)
t.left = TreeNode(4)
t.right = TreeNode(8)
t.left.left = TreeNode(11)
t.right.left = TreeNode(13)
t.right.right = TreeNode(4)
t.left.left.left = TreeNode(7)
t.left.left.right = TreeNode(2)
t.right.right.right = TreeNode(1)
s = Solution()
print(s.hasPathSum(t, 22))
