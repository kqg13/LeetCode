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
    def morrisInorderTraversal(self, root):
        """
        Do not modify original tree
        root: TreeNode
        return: List[int]
        """
        inorder = list()
        current = root
        while current is not None:
            if current.left is None:
                inorder.append(current.val)
                current = current.right
            else:
                rightmost = current.left
                rightmost = self.getRightMost(rightmost, current)
                # Link successor if not already connected
                if rightmost.right is None:
                    rightmost.right = current
                    current = current.left
                else:
                    # Reset the link to avoid modifying the tree
                    rightmost.right = None
                    inorder.append(current.val)
                    current = current.right
        return inorder

    def getRightMost(self, node, current):
        while node.right is not None and node.right != current:
            node = node.right
        return node


bst_1 = [3, 1, None, None, 2]
root1 = createTree(bst_1)
bst_2 = [2, 1, 4, None, None, 3]
root2 = createTree(bst_2)
bst_3 = [13, 6, 20, None, 7, None, 25, None, 8]
root3 = createTree(bst_3)

s = Solution()
s.morrisInorderTraversal(root1)
s.morrisInorderTraversal(root2)
s.morrisInorderTraversal(root3)
