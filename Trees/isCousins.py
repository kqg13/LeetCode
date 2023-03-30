# Easy tree problem 993: Cousins in Binary Tree

# In a binary tree, the root node is at depth 0, and children of each depth
# k node are at depth k+1. Two nodes of a binary tree are cousins if they
# have the same depth, but have different parents.
#
# We are given the root of a binary tree with unique values, and the values x
# and y of two different nodes in the tree. Return true if and only if the
# nodes corresponding to the values x and y are cousins.

from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        q = deque([(root, -1)])

        while True:
            n = len(q)
            if n == 0:
                return False
            elif n == 1:
                if q[0][0].val == x or q[0][0].val == y:
                    return False
            else:
                check = []
                for node, pval in q:
                    if node.val == x or node.val == y:
                        check.append(pval)
                if len(check) == 1:
                    return False
                elif len(check) == 2:
                    if check[0] == check[1]:
                        return False
                    else:
                        return True
            # continue
            for _ in range(n):
                node = q.popleft()[0]
                if node.left:
                    q.append((node.left, node.val))
                if node.right:
                    q.append((node.right, node.val))


# Test
r = TreeNode(1)
r.left = TreeNode(2)
r.right = TreeNode(3)
r.left.right = TreeNode(4)
s = Solution()
x1, y1 = 2, 3
print(s.isCousins(r, x1, y1))
