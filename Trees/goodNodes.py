# Tree problem 1448: Count Good Nodes in Binary Tree

# Given a binary tree root, a node X in the tree is named good if in the path
# from root to X there are no nodes with a value greater than X.
# Return the number of good nodes in the binary tree.

# https://leetcode.com/problems/count-good-nodes-in-binary-tree/


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.goodNodesCount = 0
        self.goodNodesHelper(root, root.val)
        return self.goodNodesCount

    def goodNodesHelper(self, node, maxVal):
        if node is None:
            return
        if node.val >= maxVal:
            self.goodNodesCount += 1
            maxVal = node.val
        self.goodNodesHelper(node.left, maxVal)
        self.goodNodesHelper(node.right, maxVal)


s = Solution()
t1 = TreeNode(3)
t1.left = TreeNode(1)
t1.left.left = TreeNode(3)
t1.right = TreeNode(4)
t1.right.left = TreeNode(1)
t1.right.right = TreeNode(5)
print(s.goodNodes(t1))
