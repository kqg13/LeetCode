# AlgoExpert binary tree problem: Branch Sums

# Write a function that takes in a binary tree and returns a list of branch
# sums ordered from leftmost branch sum to rightmost branch sum.


# Example: Given the below binary tree, return a list of branch sums
# [27, 22, 26, 18]

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
    def branchSums(self, root):
        if root is None: return []
        results, runningSum = [], 0
        self.branchSumsHelper(root, results, 0)
        return results

    def branchSumsHelper(self, root, results, runningSum):
        if root is None: return

        runningSum += root.val

        if root.left is None and root.right is None:
            results.append(runningSum)
            # runningSum -= root.val

        self.branchSumsHelper(root.left, results, runningSum)
        self.branchSumsHelper(root.right, results, runningSum)


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
print(s.branchSums(t))

