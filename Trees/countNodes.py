# 222: Count Complete Tree Nodes
# https://leetcode.com/problems/count-complete-tree-nodes/
# Binary search solution: https://leetcode.com/problems/count-complete-tree-nodes/solution/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def constructTree(inputTree, i, n):
    if inputTree is None: return None

    node = None

    if i < n:
        nodeVal = inputTree[i]
        node = TreeNode(nodeVal)
        node.left = constructTree(inputTree, 2 * i + 1, n)
        node.right = constructTree(inputTree, 2 * i + 2, n)

    return node


class Solution:
    # O(N)
    def countNodesNaive(self, root) -> int:
        if root is None:
            return 0
        l = self.countNodesNaive(root.left)
        r = self.countNodesNaive(root.right)
        return l + r + 1

    # Perfect binary tree check approach
    #   log(2n + 1) * log(N + 1) where 2n + 1 = # of total nodes and N + 1 = # of leaf nodes and n = # of internal nodes
    # = O(log(N) * log(N))
    # = O(log^2(N)) OR O(d^2)
    # Q. Why O(d^2)?  A. # of levels = log(2n +1)
    def countNodes(self, root) -> int:
        if root is None:
            return 0
        l_height = self.getLeftHeight(root.left)
        r_height = self.getRightHeight(root.right)
        if l_height == r_height:
            return (2 ** (l_height + 1)) - 1
        else:
            return self.countNodes(root.left) + self.countNodes(root.right) + 1

    def getLeftHeight(self, node) -> int:
        if node is None:
            return 0
        countLeft = 1
        while node.left:
            node = node.left
            countLeft += 1
        return countLeft

    def getRightHeight(self, node) -> int:
        if node is None:
            return 0
        countRight = 1
        while node.right:
            node = node.right
            countRight += 1
        return countRight


s = Solution()
r1 = [1, 2, 3, 4, 5, 6]
r2 = [1]
t1 = constructTree(r1, 0, len(r1))
t2 = constructTree(r2, 0, len(r2))
print(s.countNodes(t1))
