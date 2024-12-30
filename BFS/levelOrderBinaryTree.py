# 102: Binary Tree Level Order Traversal
# https://leetcode.com/problems/binary-tree-level-order-traversal/

from typing import List
from typing import Optional
from LeetCode.Trees import constructTreeHelper as tree_helper
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        results = list()
        if root:
            d = deque([root])

            while d:
                current_level = list()
                for _ in range(len(d)):
                    node = d.popleft()
                    current_level.append(node.val)
                    if node.left:
                        d.append(node.left)
                    if node.right:
                        d.append(node.right)

                results.append(current_level)

        return results


s = Solution()
r1 = [3, 9, 20, None, None, 15, 7]
t1 = tree_helper.createTree(r1)
s.levelOrder(t1)
r2 = [1]
t2 = tree_helper.createTree(r2)
s.levelOrder(t2)
r3 = []
t3 = tree_helper.createTree(r3)
s.levelOrder(r3)
