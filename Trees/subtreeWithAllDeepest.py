# Medium Tree Problem 865: Smallest Subtree with all the Deepest Nodes

# Given a binary tree rooted at root, the depth of each node is the shortest distance to the root.
# A node is deepest if it has the largest depth possible among any node in the entire tree.
# The subtree of a node is that node, plus the set of all descendants of that node.
# Return the node with the largest depth such that it contains all the deepest nodes in its subtree.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def subtreeWithAllDeepest(self, root):
        self.maxDepth = self.calcMaxDepth(root)
        return self.subtreeWithAllDeepestHelper(root, 0)

    def subtreeWithAllDeepestHelper(self, node, currentDepth):
        if node is None:
            return None
        if currentDepth == self.maxDepth:
            return node
        yellowL = self.subtreeWithAllDeepestHelper(node.left, currentDepth + 1)
        yellowR = self.subtreeWithAllDeepestHelper(node.right, currentDepth + 1)
        # Cases
        if yellowL is None and yellowR is None:
            yellowNode = None
        elif yellowL is None:
            yellowNode = yellowR
        elif yellowR is None:
            yellowNode = yellowL
        else:
            yellowNode = node
        return yellowNode

    def subtreeWithAllDeepestHelperRefac(self, node, currentDepth):
        if node is None:
            return None
        if currentDepth == self.maxDepth:
            return node

        yellowL = self.subtreeWithAllDeepestHelperRefac(node.left, currentDepth + 1)
        yellowR = self.subtreeWithAllDeepestHelperRefac(node.right, currentDepth + 1)
        if yellowL is None:
            return yellowR
        # Cases
        if yellowR is None:
            return yellowL
        else:
            return node

    def calcMaxDepth(self, root):
        if root is None:
            return -1
        return max(self.calcMaxDepth(root.left), self.calcMaxDepth(root.right)) + 1


s = Solution()
tree = TreeNode(3)
tree.left = TreeNode(5)
tree.right = TreeNode(1)
tree.left.left = TreeNode(6)
tree.left.right = TreeNode(2)
tree.right.left = TreeNode(0)
tree.right.right = TreeNode(8)
tree.left.right.left = TreeNode(7)
tree.left.right.right = TreeNode(4)
node = s.subtreeWithAllDeepest(tree)
print(node.val)
print(s.calcMaxDepth(tree))

