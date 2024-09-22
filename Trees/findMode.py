# 501: Find Mode in BST
# https://leetcode.com/problems/find-mode-in-binary-search-tree/

import constructTreeHelper
from collections import defaultdict


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    def findMode(self, root):
        self.maxFreq = 0
        self.currentFreq = 0
        self.currentVal = 0

        self.results = list()
        self.findModeHelper(root)

        return self.results

    def findModeHelper(self, node):
        if node:
            self.findModeHelper(node.left)

            num = node.val
            if num == self.currentVal:
                self.currentFreq += 1
            else:
                self.currentFreq = 1
                self.currentVal = num

            if self.currentFreq > self.maxFreq:
                self.maxFreq = self.currentFreq
                self.results = []

            if self.currentFreq == self.maxFreq:
                self.results.append(num)

            self.findModeHelper(node.right)

    def findModeDict(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.d = defaultdict(lambda: 0)
        self.findModeDictHelper(root)

        mode_val = max(self.d.values())

        results = [k for k, v in self.d.items() if v == mode_val]

        return results

    def findModeDictHelper(self, node):
        if node:
            self.findModeDictHelper(node.left)
            self.d[node.val] += 1
            self.findModeDictHelper(node.right)


root1 = [1, None, 2, 2, None]
root2 = [0]
root3 = [3, 2, 5]

t1 = constructTreeHelper.createTree(root1)
t2 = constructTreeHelper.createTree(root2)
t3 = constructTreeHelper.createTree(root3)

s = Solution()

s.findMode(t1)
s.findMode(t2)
s.findMode(t3)
