# Leetcode #257: Binary Tree Paths
# https://leetcode.com/problems/binary-tree-paths/


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        self.results = list()
        self.binaryTreePathsDFS(root, str(root.val))
        print(self.results)
        return self.results

    def binaryTreePathsDFS(self, node, currPath):
        if node.left is None and node.right is None:
            self.results.append(currPath)
        if node.left is not None:
            updatedPath = f"{currPath}->{node.left.val}"
            # currPath += "->" + str(node.left.val)
            self.binaryTreePathsDFS(node.left, updatedPath)
        if node.right is not None:
            updatedPath = f"{currPath}->{node.right.val}"
            # currPath += "->" + str(node.right.val)
            self.binaryTreePathsDFS(node.right, updatedPath)


t = TreeNode(1)
t.left = TreeNode(2)
t.right = TreeNode(3)
t.left.right = TreeNode(5)
s = Solution()
s.binaryTreePaths(t)
