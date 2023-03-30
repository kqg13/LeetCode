# Medium Tree Problem 105: Construct Binary Tree from
# Preorder and Inorder Traversal

# For example, given preorder = [3, 9, 20, 15, 7] and
# inorder = [9, 3, 15, 20, 7], return the following binary tree:
#     3
#    / \
#   9  20
#     /  \
#    15   7


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        rep = str(self.val)
        return rep


class Solution:
    def buildTree(self, preorder, inorder):
        """
        :param preorder: List[int]
        :param inorder: List[int]
        :return: TreeNode
        """
        if not preorder and not inorder:
            return None
        pre_length, in_length, rootval = len(preorder), len(inorder), preorder[0]

        if pre_length == 1 and in_length == 1:
            leaf = TreeNode(rootval)
            return leaf

        rootval_idx = inorder.index(rootval)
        inorder_left, inorder_right = inorder[0:rootval_idx], inorder[rootval_idx + 1:in_length]
        preorder_left, preorder_right = preorder[1:rootval_idx+1], preorder[rootval_idx+1:pre_length]

        # Construct a new TreeNode
        root = TreeNode(rootval)
        root.left = self.buildTree(preorder_left, inorder_left)
        root.right = self.buildTree(preorder_right, inorder_right)
        return root


# Test
s = Solution()
pre_order = [3, 9, 20, 15, 7]
in_order = [9, 3, 15, 20, 7]
print(s.buildTree(pre_order, in_order))
