# Easy BST problem 530: Minimum Absolute Difference in BST

# Given a binary search tree with non-negative values, find the minimum
# absolute difference between values of any two nodes.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # Time: O(N)
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.min_diff = float('inf')
        self.minvals = []

        # In-order traversal of BST will be sorted
        def inorder_helper(root):
            if root:
                inorder_helper(root.left)
                self.minvals.append(root.val)
                inorder_helper(root.right)
            return self.minvals

        def compute_min():
            for i in range(0, len(self.minvals)-1):
                self.min_diff = min(self.min_diff, self.minvals[i+1] - self.minvals[i])
            return self.min_diff

        self.minvals = inorder_helper(root)
        return compute_min()


r = TreeNode(1)
r.right = TreeNode(3)
r.right.left = TreeNode(2)
s = Solution()
print(s.getMinimumDifference(r))
