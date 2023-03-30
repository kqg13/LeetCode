# Easy tree problem 111: Minimum Depth of a Binary Tree

# Given a binary tree, find its minimum depth.
# The minimum depth is the number of nodes along the shortest path from
# the root node down to the nearest leaf node.
# Note: A leaf is a node with no children.

from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # Recursive solution O(N)
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        elif not root.left:
            return self.minDepth(root.right) + 1
        elif not root.right:
            return self.minDepth(root.left) + 1
        else:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1

    # BFS solution: we visit N/2 nodes so O(N)
    def minDepthBFS(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        d = deque([(1, root)])

        while d:
            height, root = d.popleft()
            children = [root.left, root.right]
            if not any(children):
                return height
            for child in children:
                d.append((height + 1, child))
