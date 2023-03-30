# Tree Problem 236: Lowest Common Ancestor of a Binary Tree

# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
#
# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined
# between two nodes p and q as the lowest node in T that has both p and q as descendants
# (where we allow a node to be a descendant of itself).”


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        self.lca = None
        self.lcaHelper(root, p, q)
        return self.lca

    def lcaHelper(self, node, p, q):
        if node is None:
            return False
        mid = False
        if node.val == p.val or node.val == q.val:
            mid = True
        left = self.lcaHelper(node.left, p, q)
        right = False
        if not self.lca:
            right = self.lcaHelper(node.right, p, q)
        case1and2 = mid and (left or right)  # p and q are on the same subtree (p is ancestor of q)
        case3 = left and right  # p and q are on different subtrees
        if case1and2 or case3:
            self.lca = node.val
            return True
        return left or right or mid

    def lowestCommonAncestorClean(self, root, p, q):
        # base case: leaf
        if root is None:
            return None
        # base case: if one of the nodes were found, return it
        if root == p or root == q:
            return root

        # look for both p and q in each subtree
        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)

        # case 1: if p and q found in different subtrees, then I am the LCA!
        if l and r:
            return root

        # case 2: p and q in same subtree - if you have an ancestor return it otherwise None on other side
        return l if r is None else r

    def lowestCommonAncestorKedar(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode'):
        self.ancestor = None
        self.lca_helper(root, p, q)
        return self.ancestor

    def lca_helper(self, node, p, q):
        if node is None:
            return None
        mid = node == p or node == q
        l = self.lca_helper(node.left, p, q)
        r = self.lca_helper(node.right, p, q)
        if (l and r) or (r and mid) or (l and mid):
            self.ancestor = node
        return mid or l or r

    def lcaIterative(self, root, p, q):
        stack = [root]
        parents = {root: None}
        # 1: Create parent dictionary by traversing tree using stack
        while p not in parents or q not in parents:
            node = stack.pop()
            if node.left:
                parents[node.left] = node
                stack.append(node.left)
            if node.right:
                parents[node.right] = node
                stack.append(node.right)
        # 2: Create set of p_ancestors
        p_ancestors = set()
        while p:
            p_ancestors.add(p)
            p = parents[p]
        # 3: Iterate through ancestors of q checking it it's contained in p_ancestors; if yes, return q
        while q not in p_ancestors:
            q = parents[q]
        return q

    def isInParents(self, p_or_q, parents):
        for node in parents:
            if p_or_q.val == node.val:
                return True
        return False

    def printStack(self, stack):
        print("----- Stack trace -----")
        for n in stack:
            print(n.val)


s = Solution()
t1 = TreeNode(3)
# Left
t1.left = TreeNode(5)
t1.left.left = TreeNode(6)
t1.left.right = TreeNode(2)
t1.left.right.left = TreeNode(7)
t1.left.right.right = TreeNode(4)
# Right
t1.right = TreeNode(1)
t1.right.left = TreeNode(0)
t1.right.right = TreeNode(8)
# print(s.lowestCommonAncestor(t1, TreeNode(6), TreeNode(4)))
print(s.lcaIterative(t1, TreeNode(5), TreeNode(4)))
