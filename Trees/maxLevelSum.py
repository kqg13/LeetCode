# 1161. Maximum Level Sum of a Binary Tree
# https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/

from collections import deque


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    @staticmethod
    def createTree(input_tree):
        n = len(input_tree)
        if n == 0:
            return None

        nodesQ, valsQ = list(), list()

        rootVal = input_tree[0]
        root = TreeNode(rootVal)
        nodesQ.append(root)

        for i in range(1, n):
            valsQ.append(input_tree[i])

        while valsQ:
            leftVal = valsQ.pop(0)
            rightVal = valsQ.pop(0)

            current = nodesQ.pop(0)

            if leftVal is not None:
                left = TreeNode(leftVal)
                current.left = left
                nodesQ.append(left)
            if rightVal is not None:
                right = TreeNode(rightVal)
                current.right = right
                nodesQ.append(right)
        return root

    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        level, levelSum = 1, 0
        level_list = list()
        q = deque([(level, root)])

        while q:
            n = len(q)
            for i in range(n):
                level, node = q.popleft()
                levelSum += node.val

                if i == n - 1:
                    level_list.append((level, levelSum))
                    levelSum = 0

                if node.left or node.right:
                    level += 1

                if node.left:
                    q.append((level, node.left))
                if node.right:
                    q.append((level, node.right))

        # get the max level-by-level sum
        max_sum = max(level_list, key=lambda x: x[1])[1]
        # get all levels where max sum occurs
        maxLevels_list = [j[0] for i, j in enumerate(level_list) if j[1] == max_sum]
        # get smallest level where max sum occurs
        min_level = min(maxLevels_list)
        return min_level


s = Solution()
lst = [1, 7, 0, 7, -8, None, None]
t = s.createTree(lst)
s.maxLevelSum(t)
