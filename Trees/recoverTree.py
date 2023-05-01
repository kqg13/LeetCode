# 91: Recover Tree
# https://leetcode.com/problems/recover-binary-search-tree/

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
    def recoverTree(self, root) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        inorder = self.getOriginalInorder(root, [])
        first, second = self.getSwappedElements(inorder)
        inorder[first].val, inorder[second].val = inorder[second].val, inorder[first].val

    def getOriginalInorder(self, root, inorder):
        if root:
            self.getOriginalInorder(root.left, inorder)
            inorder.append(root)
            self.getOriginalInorder(root.right, inorder)
        return inorder

    def getSwappedElements(self, lst):
        first = second = None
        for i in range(1, len(lst)):
            if lst[i].val < lst[i - 1].val:
                if first is None:
                    first = i - 1
                    second = i
                else:
                    second = i
        return first, second

    def recoverTreeMorrisOrder(self, root) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.morrisInorderTraversal(root)

    def morrisInorderTraversal(self, root):
        """
        Do not modify original tree
        """
        current = root
        first = second = pred = None
        while current is not None:
            if current.left is None:
                # check here for violation
                if pred is not None and current.val < pred.val:
                    second = current
                    if first is None:
                        first = pred
                pred = current

                current = current.right
            else:
                rightmost = current.left
                rightmost = self.getRightMost(rightmost, current)
                # Link successor if not already connected
                if rightmost.right is None:
                    rightmost.right = current
                    current = current.left
                else:
                    # check here for violation
                    if pred is not None and current.val < pred.val:
                        second = current
                        if first is None:
                            first = pred
                    pred = current

                    # Reset the link to avoid modifying the tree
                    rightmost.right = None
                    current = current.right
        # Swap
        first.val, second.val = second.val, first.val

    def getRightMost(self, node, current):
        while node.right is not None and node.right != current:
            node = node.right
        return node


t1 = [1, 3, None, None, 2]
root1 = createTree(t1)
t2 = [3, 1, 4, None, None, 2]
root2 = createTree(t2)
t3 = [13, 6, 20, None, 7, 8, 25]
root3 = createTree(t3)

s = Solution()
# s.recoverTree(root1)
s.recoverTreeMorrisOrder(root1)

# s.recoverTree(root2)
s.recoverTreeMorrisOrder(root2)
