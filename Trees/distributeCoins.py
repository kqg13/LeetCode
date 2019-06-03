# Medium tree problem 979: Distribute Coins in a Binary Tree
# https://leetcode.com/problems/distribute-coins-in-binary-tree/

# Given the root of a binary tree with N nodes, each node in the tree has
# node.val coins, and there are N coins total. In one move, we may choose two
# adjacent nodes and move one coin from one node to another.  (The move may be
# from parent to child, or from child to parent.)
# Return the number of moves required to make every node have exactly one coin.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def distributeHelper(self, root, moveCount=0, rc=True):
        """
        :param root: TreeNode
        :return: int
        """
        bl, br = 0, 0

        if root.left:
            bl, moveCount = self.distributeHelper(root.left, moveCount, False)

        if root.right:
            br, moveCount = self.distributeHelper(root.right, moveCount, False)

        balance = bl + br + abs(root.val - 1)
        if not rc: moveCount += balance
        print("balance: ", balance, "mc: ", moveCount)
        return balance, moveCount

    def distributeCoins(self, root):
        return self.distributeHelper(root)[1]


t = TreeNode(4)
t.left = TreeNode(0)
t.left.right = TreeNode(0)
t.left.right.right = TreeNode(0)

# t = TreeNode(1)
# t.val = 1
# t.left = TreeNode(0)
# t.left.val = 0
# t.right = TreeNode(0)
# t.right.val = 0
# t.left.right = TreeNode(3)
# t.left.right.val = 3
s = Solution()
print(s.distributeCoins(t))
