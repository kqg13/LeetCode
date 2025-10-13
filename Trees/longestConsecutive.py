# 298: Binary Tree Longest Consecutive Sequence
# https://leetcode.com/problems/binary-tree-longest-consecutive-sequence/description/?envType=problem-list-v2&envId=tree

from typing import Optional
import constructTreeHelper as th


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        self.result = 1
        self.longestConsecutiveHelper(parentVal=float('-inf'), node=root, currentStreak=0)
        return self.result

    def longestConsecutiveHelper(self, parentVal, node, currentStreak):
        if node is None:
            return
        if node.val - parentVal == 1:
            currentStreak += 1
            self.result = max(currentStreak, self.result)
        else:
            currentStreak = 1
        self.longestConsecutiveHelper(node.val, node.left, currentStreak)
        self.longestConsecutiveHelper(node.val, node.right, currentStreak)


s = Solution()
root1 = [1, None, 3, 2, 4, None, None, None, 5]
root2 = [2, None, 3, 2, None, 1]
tree1 = th.createTree(root1)
tree2 = th.createTree(root2)
s.longestConsecutive(tree1)
