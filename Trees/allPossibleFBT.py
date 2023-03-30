# Medium Tree Problem 894: All Possible Full Binary Trees
# Preorder and Inorder Traversal

# A full binary tree is a binary tree where each node has exactly
# 0 or 2 children. Return a list of all possible full binary trees with
# N nodes.  Each element of the answer is the root node of one possible
# tree.

# Each node of each tree in the answer must have node.val = 0.
# You may return the final list of trees in any order.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        rep = str(self.val)
        return rep


class Solution:
    def allPossibleFBT(self, N):
        return 0


s = Solution()
print(s.allPossibleFBT(7))
