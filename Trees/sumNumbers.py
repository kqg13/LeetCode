# 129: Sum Root to Leaf Numbers
# https://leetcode.com/problems/sum-root-to-leaf-numbers/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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


class Solution:
    def sumNumbers(self, root) -> int:
        self.result = 0
        self.sumNumbersHelper(root, currentSum=0)
        return self.result

    def sumNumbersHelper(self, node, currentSum):
        if node:
            currentSum = (10 * currentSum) + node.val
            if not node.left and not node.right:
                self.result += currentSum

            if node.left:
                self.sumNumbersHelper(node.left, currentSum)
            if node.right:
                self.sumNumbersHelper(node.right, currentSum)

    def sumNumbersPaths(self, root):
        self.all_paths = list()
        result = 0

        self.sumNumbersPathsHelper(root, [])

        for path in self.all_paths:
            result += int(''.join(str(node_val) for node_val in path))
        return result

    def sumNumbersPathsHelper(self, node, current_path):
        if not node.left and not node.right:
            current_path.append(node.val)
            self.all_paths.append(current_path.copy())
            current_path.pop()
            return

        current_path.append(node.val)

        if node.left:
            self.sumNumbersPathsHelper(node.left, current_path)

        if node.right:
            self.sumNumbersPathsHelper(node.right, current_path)

        current_path.pop()


r1 = [1, 2, 3]
r2 = [4, 9, 0, 5, 1]
r3 = [1, 5, 2, None, None, 3, 4]
r4 = [1, None, 2, 3, 4]
r5 = [4, 9, 0, None, 1]
r6 = [0, 1, 2, 3, 4, 3, 4]

t1 = createTree(r1)
t2 = createTree(r2)
t3 = createTree(r3)
t4 = createTree(r4)
t5 = createTree(r5)
t6 = createTree(r6)
