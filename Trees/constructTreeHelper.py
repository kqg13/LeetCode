# This is a LeetCode helper function to construct a binary tree from a given input string
# Approach: if root is at i, left node is 2i + 1 and right node is 2i + 2


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# This works only for a complete binary tree (every level except possibly last is filled and leaves are leftmost)
# https://web.cecs.pdx.edu/~sheard/course/Cs163/Doc/FullvsComplete.html
# https://stackoverflow.com/questions/37941318/how-to-build-an-incomplete-binary-tree-from-array-representation
def constructTree(inputTree, i, n):
    if inputTree is None: return None

    node = None

    if i < n:
        nodeVal = inputTree[i]
        node = TreeNode(nodeVal)
        node.left = constructTree(inputTree, 2 * i + 1, n)
        node.right = constructTree(inputTree, 2 * i + 2, n)

    return node


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


root = [3, 9, 20, None, None, 15, 7]
tree = constructTree(root, 0, len(root))
print(tree.val, tree.left.val, tree.right.val, tree.right.left.val, tree.right.right.val)
root2 = [3, 1, 4, None, None, 2]
tree2 = createTree(root2)
