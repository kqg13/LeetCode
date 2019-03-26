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
        self.in_dict = {val: i for i, val in enumerate(inorder)}
        pre_start, in_start = 0, 0
        pre_end, in_end = len(preorder) - 1, len(inorder) - 1

        def tree_helper(pre_start, pre_end, preorder, in_start, in_end, inorder):
            if pre_start > pre_end or in_start > in_end: return

            root = TreeNode(preorder[pre_start])
            # Find root index
            root_index = self.in_dict[root.val]

            root.left = tree_helper(pre_start + 1, pre_start + root_index, preorder,
                                    in_start, root_index - 1, inorder)

            root.right = tree_helper(pre_start+(root_index - in_start) + 1, pre_end, preorder,
                                     root_index + 1, in_end, inorder)

            return root

        return tree_helper(pre_start, pre_end, preorder, in_start, in_end, inorder)


# Test
s = Solution()
# pre_order = [3, 9, 20, 15, 7]
# in_order = [9, 3, 15, 20, 7]
pre_order = [1, 2, 3]
in_order = [2, 3, 1]
print(s.buildTree(pre_order, in_order))
