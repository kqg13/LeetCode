from collections import defaultdict
# 863: All Nodes Distance K in Binary Tree
# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/description/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    @staticmethod
    def createTree(inputTree):
        n = len(inputTree)
        if n == 0:
            return None

        nodesQ, valsQ = list(), list()

        rootVal = inputTree[0]
        root = TreeNode(rootVal)
        nodesQ.append(root)

        for i in range(1, n):
            valsQ.append(inputTree[i])

        while valsQ:
            if valsQ:
                leftVal = valsQ.pop(0)
            if valsQ:
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

    def distanceK(self, root, target, k):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        """
        self.graph = defaultdict(lambda: list())
        self.buildGraph(root, None)
        self.results = list()
        self.dfs(target.val, 0, k, set())
        return self.results

    def dfs(self, node_val, n, k, visited):
        visited.add(node_val)
        if n == k:
            self.results.append(node_val)
        for neighbor in self.graph[node_val]:
            if neighbor not in visited:
                self.dfs(neighbor, n + 1, k, visited)

    def buildGraph(self, node, parent):
        if parent:
            self.graph[node.val].append(parent.val)
        if node.left:
            self.graph[node.val].append(node.left.val)
            self.buildGraph(node.left, node)
        if node.right:
            self.graph[node.val].append(node.right.val)
            self.buildGraph(node.right, node)


s = Solution()
t1, target1, k1 = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 2  # Expected: [7, 4, 1]
root1 = s.createTree(t1)
s.distanceK(root1, root1.left, k1)

t2, target2, k2 = [1], 1, 3   # Expected: []
root2 = s.createTree(t2)
s.distanceK(root2, root2, k2)
