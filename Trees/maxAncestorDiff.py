# Medium Tree Problem 1026: Maximum Difference Between Node and Ancestor

# Given the root of a binary tree, find the maximum value V for which there
# exists different nodes A and B where V = |A.val - B.val| and A is an ancestor
# of B. (A node A is an ancestor of B if either: any child of A is equal to B,
# or any child of A is an ancestor of B.)


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        self.global_max = 0
        path_min, path_max = root.val, root.val
        self.maxAncestorDiffHelper(root, path_min, path_max)
        return self.global_max

    def maxAncestorDiffHelper(self, node, path_min, path_max):
        if node is not None:
            path_min = min(path_min, node.val)
            path_max = max(path_max, node.val)
            self.global_max = max(self.global_max, abs(node.val - path_min), abs(node.val - path_max))
            self.maxAncestorDiffHelper(node.left, path_min, path_max)
            self.maxAncestorDiffHelper(node.right, path_min, path_max)


t = TreeNode(8)
t.left = TreeNode(3)
t.left.left = TreeNode(1)
t.left.right = TreeNode(6)
t.left.right.left = TreeNode(4)
t.left.right.right = TreeNode(7)

t.right = TreeNode(10)
t.right.right = TreeNode(14)
t.right.right.left = TreeNode(13)


s = Solution()
print(s.maxAncestorDiff(t))
