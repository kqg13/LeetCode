# Easy tree problem 637: Average of Levels in Binary Tree

# Given a non-empty binary tree, return the average value of the nodes on each
# level in the form of an array.

# Definition for a binary tree node.

from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def averageOfLevels(self, root):
        """
        :param root: TreeNode
        :return: List[Float]
        """
        curr_level = 0
        level = 0
        d = deque([(root, level)])

        curr_total, counter = 0, 0
        results = []

        while d:
            node, level = d.popleft()
            if level == curr_level:
                counter += 1
                curr_total += node.val
            else:
                results.append(curr_total / counter)
                counter = 1
                curr_level = level
                curr_total = node.val

            if node.left:
                d.append((node.left, curr_level + 1))
            if node.right:
                d.append((node.right, curr_level + 1))

        results.append(curr_total/ counter)
        return results


r = TreeNode(3)
r.left = TreeNode(9)
r.right = TreeNode(20)
r.right.left = TreeNode(15)
r.right.right = TreeNode(7)
