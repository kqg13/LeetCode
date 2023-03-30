# Easy BFS binary tree problem 107: Binary Tree Level Order Traversal II

# Given a binary tree, return the bottom-up level order traversal of its nodes'
# values. (ie, from left to right, level by level from leaf to root).

from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        d = deque([root])
        output = []

        while d:
            level = []
            for _ in range(len(d)):
                curr = d.popleft()
                if curr.left: d.append(curr.left)
                if curr.right: d.append(curr.right)
                level.append(curr.val)
            output.append(level)

        return output[::-1]
