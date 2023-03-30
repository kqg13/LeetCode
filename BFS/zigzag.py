# 103. Binary Tree Zigzag Level Order Traversal

# Given the root of a binary tree, return the zigzag level order traversal of its nodes' values.
# (i.e., from left to right, then right to left for the next level and alternate between).

from collections import deque


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        results = list()
        reverse = False
        q = deque([root])
        while q:
            current = []
            for _ in range(len(q)):
                node = q.popleft()
                current.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if reverse:
                results.append(current[::-1])
            else:
                results.append(current)
            reverse = not reverse
        return results


s = Solution()
t = TreeNode(3)
t.left = TreeNode(9)
t.right = TreeNode(20)
t.right.left = TreeNode(15)
t.right.right = TreeNode(7)
print(s.zigzagLevelOrder(t))
