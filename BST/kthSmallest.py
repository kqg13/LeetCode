# LeetCode 230: kth Smallest Element in a BST

# Given the root of a binary search tree, and an int k, return the kth (1-indexed)
# smallest element in the tree.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Time: O(N) Space: O(N)
    def kthSmallest(self, root, k):
        """
        :param root:
        :param k: int
        :return: int
        """
        return self.kthSmallestHelper(root, k, [])[k - 1]

    def kthSmallestHelper(self, node, k, results):
        if node is None:
            return
        self.kthSmallestHelper(node.left, k, results)
        results.append(node.val)
        self.kthSmallestHelper(node.right, k, results)
        return results

    # Time: O(d + k), Space: O(d) where d is depth of tree
    # Why?
    # First we need to get to the smallest element (leaf) of BST which will require height of tree
    # After that we will need to
    def kthSmallestIterative(self, root, k):
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            else:
                root = root.right


s = Solution()
t = TreeNode(5)
t.left = TreeNode(3)
t.right = TreeNode(6)
t.left.left = TreeNode(2)
t.left.right = TreeNode(4)
t.right.right = TreeNode(7)

k1 = 3
print(s.kthSmallestIterative(t, k1))
