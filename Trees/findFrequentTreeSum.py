# 508: Most Frequent Subtree Sum
# https://leetcode.com/problems/most-frequent-subtree-sum/

from collections import defaultdict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findFrequentTreeSum(self, root):
        self.freq_dict = defaultdict(lambda: 0)
        self.preOrder(root)
        max_freq = max(self.freq_dict.values())
        all_max_vals = [k for k, v in self.freq_dict.items() if v == max_freq]
        return all_max_vals

    def preOrder(self, node):
        if node:
            subTreeSum = self.getSubTreeSum(node)
            self.freq_dict[subTreeSum] += 1
            self.preOrder(node.left)
            self.preOrder(node.right)

    def getSubTreeSum(self, node):
        """
        node: TreeNode
        return: int
        """
        if node is None:
            return 0

        rootVal = node.val
        leftVal = self.getSubTreeSum(node.left)
        rightVal = self.getSubTreeSum(node.right)
        return rootVal + leftVal + rightVal
