# 1302: Deepest Leaves Sum


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructTree(self, inputTree, i, node):
        if inputTree is None:
            return None

        leftIdx = 2 * i + 1
        rightIdx = 2 * i + 2

        if node is not None:

            if leftIdx < len(inputTree):
                if inputTree[leftIdx] is None:
                    node.left = None
                else:
                    node.left = TreeNode(inputTree[leftIdx])
                self.constructTree(inputTree, leftIdx, node.left)

            if rightIdx < len(inputTree):
                if inputTree[rightIdx] is None:
                    node.right = None
                else:
                    node.right = TreeNode(inputTree[rightIdx])
                self.constructTree(inputTree, rightIdx, node.right)

    def createTree(self, inputTree):
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

    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.currentSum = 0
        self.deepest = 0
        self.deepestLeavesSumHelper(root, 0)
        return self.currentSum

    def deepestLeavesSumHelper(self, node, depth):
        if node.left is None and node.right is None:
            # Case 1: we are at the deepest
            if depth > self.deepest:
                self.currentSum = node.val
                self.deepest = depth
            # Case 2: we are the same (equal) deepest
            elif depth == self.deepest:
                self.currentSum += node.val
            # Case 3: we are at another leaf - do nothing
        if node.left:
            self.deepestLeavesSumHelper(node.left, depth + 1)
        if node.right:
            self.deepestLeavesSumHelper(node.right, depth + 1)


s = Solution()
root1Lst = [1, 2, 3, 4, 5, None, 6, 7, None, None, None, None, 8]
# s.constructTree(root1Lst, 0, root1)
root1 = TreeNode(root1Lst[0])
s.constructTree(root1Lst, 0, root1)
# root1 = s.createTree(root1Lst)
print("test 1: ", s.deepestLeavesSum(root1))

root2Lst = [6, 7, 8, 2, 7, 1, 3, 9, None, 1, 4, None, None, None, 5]
# # s.constructTree(root2Lst, 0, root2)
root2 = s.createTree(root2Lst)
print(s.deepestLeavesSum(root2))
#
root3Lst = [1, 2, 3]
root3 = s.createTree(root3Lst)
print(s.deepestLeavesSum(root3))

root4Lst = [1, 2, 3, None, None, None, 5]
# root4 = s.createTree(root4Lst)
root4 = TreeNode(root4Lst[0])
s.constructTree(root4Lst, 0, root4)
print("test 4: ", s.deepestLeavesSum(root4))

root5Lst = [5, 4, 8, 11, None, 17, 4, 7, None, None, None, None, None, 5, None]
# root4 = s.createTree(root4Lst)
# root5 = TreeNode(root5Lst[0])
# s.constructTree(root5Lst, 0, root5)
root5 = s.createTree(root5Lst)
print("test 5: ", s.deepestLeavesSum(root5))
