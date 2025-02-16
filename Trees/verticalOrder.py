# 314: Binary Tree Vertical Order Traversal
# https://leetcode.com/problems/binary-tree-vertical-order-traversal/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days

from typing import List
from typing import Optional
import constructTreeHelper
from collections import defaultdict
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        d = defaultdict(lambda: list())
        queue = deque([(root, 0)])
        while queue:
            node_tuple = queue.popleft()
            node, node_col = node_tuple
            d[node_col].append(node.val)

            if node.left:
                left_col = node_col - 1
                queue.append((node.left, left_col))

            if node.right:
                right_col = node_col + 1
                queue.append((node.right, right_col))

        results = [d[k] for k in sorted(d)]
        return results


s = Solution()
root1 = [3, 9, 20, None, None, 15, 7]
t1 = constructTreeHelper.createTree(root1)
