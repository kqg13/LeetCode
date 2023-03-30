# 662: Maximum Width of a Binary Tree

# Given a binary tree, write a function to get the maxi width of the given tree.
# The maximum width of a tree is the maximum width among all levels.

# The width of one level is defined as the length between the
# end-nodes (the leftmost and right most non-null nodes in the level, where the
# null nodes b/w the end-nodes are also counted into the length calculation.

# Output: 4
#            1
#          /   \
#         3     2
#        / \     \
#       5   3     9
# Output: 4

# Output: 8
#           1
#          / \
#         3   2
#        /     \
#       5       9
#      /         \
#     6           7


from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def widthOfBinaryTree(self, root):
        """
        :param root: TreeNode
        :return: int
        """
        if root is None: return 0
        q = deque([(root, 1)])
        maxwidth = 1
        while q:
            if len(q) > 1:
                firstEle, lastEle = q[0][1], q[-1][1]
                maxwidth = max(maxwidth, lastEle - firstEle + 1)
            for i in range(len(q)):
                node, number = q.popleft()
                if node.left:
                    q.append((node.left, 2 * number))
                if node.right:
                    q.append((node.right, 2 * number + 1))
        return maxwidth


s = Solution()
t1 = TreeNode(1)
t1.left = TreeNode(3)
t1.right = TreeNode(2)
t1.left.left = TreeNode(5)
t1.left.right = TreeNode(3)
t1.right.right = TreeNode(9)
print(s.widthOfBinaryTree(t1))
