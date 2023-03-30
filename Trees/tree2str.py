# Easy tree problem 606: Construct String from Binary Tree

# Construct a string consists of parenthesis and integers from a bimary
# tree with the preorder traversing way. The null node needs to be
# represented by empty parenthesis pair "()". And you need to omit all the
# empty parenthesis pairs that don't affect the 1-to-1 mapping
# relationship b/w the string and the original binary tree.

# Example:
# Input: Binary tree: [1,2,3,4]
#        1
#      /   \
#     2     3
#    /
#   4
# Output: "1(2(4))(3)"


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def tree2str(self, t):
        """
        :param t: TreeNode
        :return: str
        """
        string = ""
        if t is not None:
            if t.left is None and t.right is None:
                string = str(t.val)
            elif t.left and t.right:
                str_l = self.tree2str(t.left)
                str_r = self.tree2str(t.right)
                string = "{}({})({})".format(t.val, str_l, str_r)
            elif t.left:
                str_l = self.tree2str(t.left)
                string = "{}({})".format(t.val, str_l)
            elif t.right:
                str_r = self.tree2str(t.right)
                string = "{}()({})".format(t.val, str_r)
        return string


# Test
r = TreeNode(1)
r.left = TreeNode(2)
r.right = TreeNode(3)
r.left.right = TreeNode(4)
s = Solution()
print(s.tree2str(r))
