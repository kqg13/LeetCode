# Medium BST problem 938: Range Sum BST

# Given the root node of a binary search tree, return the sum of values of all
# nodes with value between L and R (inclusive).
#
# The binary search tree is guaranteed to have unique values.


from bisect import bisect_left, bisect


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        self.traversal = []

        def inorder_helper(root):
            if root:
                inorder_helper(root.left)
                if root.val is not None:
                    self.traversal.append(root.val)
                inorder_helper(root.right)
            return self.traversal

        def get_sum():
            return sum(self.traversal[bisect_left(self.traversal, L):bisect(self.traversal, R)])

        self.traversal = inorder_helper(root)
        return get_sum()

    def rangeSumBSTdfs(self, root, L, R):
        self.ans = 0

        def dfs(node):
            if node:
                if L <= node.val <= R:
                    self.ans += node.val
                if L < node.val:
                    dfs(node.left)
                if node.val < R:
                    dfs(node.right)

        dfs(root)
        return self.ans


s = Solution()
r = TreeNode(10)
r.left = TreeNode(5)
r.left.left = TreeNode(3)
r.left.right = TreeNode(7)
r.right = TreeNode(15)
r.right.right = TreeNode(18)
print(s.rangeSumBSTdfs(r, 7, 15))
