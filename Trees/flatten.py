# 114: Flatten Binary Tree to Linked List
# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/description/


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        pass

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


s = Solution()
root1 = [1, 2, 5, 3, 4, None, 6]
tree1 = s.createTree(root1)
flattened = s.flatten(tree1)

# print(tree1.val, tree1.left.val, tree1.left.left.val, tree1.left.right.val, tree1.right.val, tree1.right.right.val)
# root2 = [3, 9, 20, None, None, 15, 7]
# tree2 = s.createTree(root2)
