# Easy tree problem 872: Leaf-similar Trees

# Two binary trees are considered leaf-similar if their leaf value sequence
# is the same.
#
# Return true if and only if the two given trees with head nodes root1
# and root2 are leaf-similar.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def leafSimilar(self, root1, root2):
        """
        :param root1: TreeNode
        :param root2: TreeNode
        :return: bool
        """

        def dfs(node, lst):
            if node:
                if not node.left and not node.right:
                    lst.append(node.val)
                dfs(node.left, lst)
                dfs(node.right, lst)

        t1_lst, t2_lst = [], []
        dfs(root1, t1_lst)
        dfs(root2, t2_lst)
        return t1_lst == t2_lst
