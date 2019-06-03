# Easy tree problem 543: Diameter of a binary tree
# https://leetcode.com/problems/diameter-of-binary-tree/

# Given a binary tree, you need to compute the length of the diameter of the
# tree. The diameter of a binary tree is the length of the longest path b/w any
# two nodes in a tree. This path may or may not pass through the root.

#         1
#        / \
#       2   3
#      / \
#     4   5
# Output: return 3 which is the length of [4, 2, 1, 3] or [5, 2, 1, 3]


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def diameterOfBinaryTree(self, root):
        return max(self.diameterHelper(root))

    def diameterHelper(self, root):
        """
        :param root: TreeNode
        :return: int
        """
        if root is None:
            return (-1, 0)

        lBranch, lTriangle = self.diameterHelper(root.left)
        rBranch, rTriangle = self.diameterHelper(root.right)
        bestBranch = max(lBranch, rBranch) + 1
        bestSubTriangle = max(lTriangle, rTriangle)
        bestTriangle = max(lBranch + rBranch + 2, bestSubTriangle)
        # print("left: ", lBranch, "right: ", rBranch, "bestBranch: ", bestBranch, "bestSub: ", bestSubTriangle, "bestTri: ", bestTriangle)
        return bestBranch, bestTriangle


s = Solution()
t = TreeNode(1)
t.left = TreeNode(2)
t.right = TreeNode(3)
t.left.left = TreeNode(4)
t.left.right = TreeNode(5)

print(s.diameterOfBinaryTree(t))

