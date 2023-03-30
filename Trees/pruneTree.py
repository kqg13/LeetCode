# Medium Tree Problem 814: Binary Tree Pruning

# We are given the head node root of a binary tree, where additionally
# every node's value is either a 0 or a 1.
# Return the same tree where every subtree (of the given tree) not containing
# a 1 has been removed. Recall that the subtree of a node X is X, plus
# every node that is a descendant of X.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.treelist = []

    def __str__(self):
        return ', '.join(self.treelist)

    def traverse(self):
        if self:
            self.traverse(x.left)
            self.traverse(right)
            self.treelist.append(self.val)


class Solution:
    def pruneTree(self, root):
        if root is None:
            return None

        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)

        if root.left is None and root.right is None and root.val == 0:
            return None  # Reset root node
        else:
            return root


t = TreeNode(1)
t.right = TreeNode(0)
t.right.left = TreeNode(0)
t.right.right = TreeNode(1)
s = Solution()
print(s.pruneTree(t))
