# 988: Smallest String Starting from Leaf
# https://leetcode.com/problems/smallest-string-starting-from-leaf/
# https://leetcode.com/problems/smallest-string-starting-from-leaf/discuss/2969425/Python3-concise-solution-beats-99

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
    def smallestFromLeaf(self, root) -> str:
        self.paths = list()
        self.smallestFromLeafHelper(root, str())
        sorted_paths = sorted(self.paths)
        print("sorted_paths: ", sorted_paths)
        return sorted_paths[0]

    def smallestFromLeafHelper(self, node, current):
        if not node.left and not node.right:
            alpha = chr(node.val + 97)
            current += alpha
            reversed_current = current[::-1]
            self.paths.append(reversed_current)
            current = current[:-1]
            return

        alpha = chr(node.val + 97)
        current += alpha

        if node.left:
            self.smallestFromLeafHelper(node.left, current)

        if node.right:
            self.smallestFromLeafHelper(node.right, current)

        current = current[:-1]


r1 = [0, 1, 2, 3, 4, 3, 4]  # Expected: dba
r2 = [25, 1, 3, 1, 3, 0, 2]  # Expected: adz
r3 = [2, 2, 1, None, 1, 0, None, 0]  # Expected: abc

t1 = createTree(r1)
t2 = createTree(r2)
t3 = createTree(r3)

s = Solution()
