# Medium Tree Problem 366: Find Leaves of Binary Tree

# Given a binary tree, collect a tree's nodes as if you were doing this:
# Collect and remove all leaves, repeat until the tree is empty.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findLeaves(self, root):
        output = []
        self.findLeavesHelper(root, output)
        return output

    def findLeavesHelper(self, root, output):
        if root is None:
            return -1

        maxLeft, maxRight = self.findLeavesHelper(root.left, output), self.findLeavesHelper(root.right, output)
        maxLevel = max(maxLeft, maxRight) + 1
        if maxLevel > len(output) - 1:
            output.append([])
        output[maxLevel].append(root.val)
        return maxLevel


t = TreeNode(1)
t.left = TreeNode(2)
t.right = TreeNode(3)
t.left.left = TreeNode(4)
t.left.left.left = TreeNode(6)
t.left.right = TreeNode(5)
s = Solution()
print(s.findLeaves(t))
