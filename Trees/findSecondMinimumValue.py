# 671: Second Minimum Node In a Binary Tree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return -1
        m1 = root.val
        m2 = self.findMin2(root, m1, m1)
        return self.checkMins(m1, m2)

    def findMin2(self, node, curr_m2, m1):
        # case 1: no children
        if node.left is None:
            return root.val
        # search right
        if node.left.val > node.right.val:
            curr_m2 = node.left.val
            m2 = self.findMin2(node.right, curr_m2, m1)
        # search left
        elif node.right.val > node.left.val:
            curr_m2 = node.right.val
            m2 = self.findMin2(node.left, curr_m2, m1)
        else:  # equal subtrees
            m2_right = self.findMin2(node.right, curr_m2, m1)
            m2_left = self.findMin2(node.left, curr_m2, m1)
            m2_min = min(m2_left, m2_right)
            if m2_min != m1:
                return m2_min
            else:
                return max(m2_left, m2_right)
        if min(m2, curr_m2) != m1:
            return min(m2, curr_m2)
        else:
            return max(m2, curr_m2)

    def checkMins(self, m1, m2):
        return -1 if m1 == m2 else m2


root = TreeNode(2)
root.left = TreeNode(2)
root.right = TreeNode(2)
# root.right.left = TreeNode(2)
# root.right.right = TreeNode(7)
s = Solution()
print(s.findSecondMinimumValue(root))

