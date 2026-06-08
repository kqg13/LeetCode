# 513: Find Bottom Left Value
# https://leetcode.com/problems/find-bottom-left-tree-value/description/?envType=problem-list-v2&envId=tree

import constructTreeHelper
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findBottomLeftValue(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if root:
            d = deque([root])

            while d:
                leftmost = d[0]
                for _ in range(len(d)):
                    node = d.popleft()
                    if node.left:
                        d.append(node.left)
                    if node.right:
                        d.append(node.right)

        return leftmost.val


s = Solution()
root1 = [2, 1, 3]
root2 = [1, 2, 3, 4, None, 5, 6, None, None, 7]
t2 = constructTreeHelper.createTree(root2)
