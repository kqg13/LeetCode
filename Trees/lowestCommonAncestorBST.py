# 235: Lowest Common Ancestor of a Binary Search Tree
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/?envType=problem-list-v2&envId=tree


import constructTreeHelper as th


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # base case: leaf
        if root is None:
            return None
        # base case: if one of the nodes were found, return it
        if root == p or root == q:
            return root
        # base case
        if (p.val < root.val < q.val) or (q.val < root.val < p.val):
            return root

        # look for both p and q in each subtree
        if p.val < root.val and q.val < root.val:
            l = self.lowestCommonAncestor(root.left, p, q)
            return l
        elif p.val > root.val and q.val > root.val:
            r = self.lowestCommonAncestor(root.right, p, q)
            return r


s = Solution()

root2 = [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]
p2 = TreeNode(2)
q2 = TreeNode(4)  # Expected: 4
tree2 = th.createTree(root2)

lca2 = s.lowestCommonAncestor(tree2, p2, q2)
print(lca2)
print(lca2.val)
