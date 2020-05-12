# Medium Tree Problem 337: House Robber III

# The thief has found himself a new place for his thievery again. There is only
# one entrance to this area, called the "root." Besides the root, each house
# has one and only one parent house. After a tour, the smart thief realized
# that "all houses in this place forms a binary tree". It will automatically
# contact the police if two directly-linked houses were broken into on the same night.

# Determine the max amount of money the thief can rob tonight without
# alerting the police.

# Input: [3, 4, 5, 1, 3, null, 1]
#     3
#    / \
#   4   5
#  / \   \
# 1   3   1

# Output: 9
# Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rob(self, root):
        result = self.robHelper(root)
        return max(result)

    def robHelper(self, node):
        if node:
            resultL, resultR = self.robHelper(node.left), self.robHelper(node.right)
            # Exclude: sum of the max excludes
            r0 = max(resultL) + max(resultR)
            # Include: node plus the excludes
            r1 = node.val + resultL[0] + resultR[0]
            return (r0, r1)
        else:
            return (0, 0)


s = Solution()
tree = TreeNode(3)
tree.left = TreeNode(4)
tree.left.left = TreeNode(1)
tree.left.right = TreeNode(3)
tree.right = TreeNode(5)
tree.right.right = TreeNode(1)
print(s.rob(tree))