# Practice

# Given a binary tree and a sum, list all branches in a tree


# Example: Given the below binary tree, return a list of
# [[5, 4, 11, 7], [5, 4, 11, 2], [5, 8, 13], [5, 8, 4, 1]]

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
    def listBranches(self, root):
        self.results, stack = [], []
        self.listBranchesHelper(root, stack)
        return self.results

    def listBranchesHelper(self, root, stack):
        if root is None:
            return

        stack.append(root.val)
        if root.left is None and root.right is None:
            self.results.append(stack[:])

        self.listBranchesHelper(root.left, stack)
        self.listBranchesHelper(root.right, stack)
        stack.pop()

    def maxDepth(self, root):
        if root is None:
            return 0
        return max(self.maxDepth(root.left) + 1, self.maxDepth(root.right) + 1)


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
print(s.listBranches(t))
print(s.maxDepth(t))
