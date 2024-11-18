# 156: Binary Tree Upside Down
# https://leetcode.com/problems/binary-tree-upside-down/

# Create tree from list
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


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def upsideDownBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if root:
            new_root, _ = self.upsideDownBinaryTreeDfs(root)
            return new_root
        return None

    def upsideDownBinaryTreeDfs(self, node):
        if node.left is None:
            return node, node

        new_root, right_most = self.upsideDownBinaryTreeDfs(node.left)
        right_most.left = node.right
        right_most.right = TreeNode(node.val)

        return new_root, right_most.right

    def upsideDownBinaryTreeClean(self, root):
        if root:
            return self.recurse(root, None, None)
        return None

    def recurse(self, node, parent=None, right=None):
        if not node:
            return parent
        res = self.recurse(node.left, node, node.right)
        node.right = parent
        node.left = right
        return res


root1, root2 = [1, 2, 3, 4, 5], [1]
t1 = createTree(root1)
s = Solution()
tree1 = s.upsideDownBinaryTreeClean(t1)
