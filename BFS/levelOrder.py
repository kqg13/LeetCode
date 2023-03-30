# Easy tree problem 429: N-ary Tree Level Order Traversal

# Given an n-ary tree, return the level order traversal of its nodes' values
# (i.e, from left to right, level by level).

from collections import deque


# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root):
        """
        :type root: Node
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
                level.append(curr.val)
                d.extend(curr.children)

            output.append(level)

        return output
