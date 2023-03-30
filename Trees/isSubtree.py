# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        sequenceS, sequenceT = [], []
        self.preOrder(s, sequenceS)
        self.preOrder(t, sequenceT)
        return self.isSubString(sequenceS, sequenceT)

    def preOrder(self, root, sequence):
        if root is None:
            sequence.append(None)
        else:
            sequence.append(root.val)
            self.preOrder(root.left, sequence)
            self.preOrder(root.right, sequence)

    def listToString(self, lst):
        str_list = ', '.join(map(str, lst))
        return ', ' + str_list

    def isSubString(self, lst1, lst2):
        str1 = self.listToString(lst1)
        str2 = self.listToString(lst2)
        # print(str1, str2)
        return str2 in str1


t1 = TreeNode(3)
t1.left = TreeNode(4)
t1.right = TreeNode(5)
t1.left.left = TreeNode(1)
t1.left.right = TreeNode(2)

t2 = TreeNode(4)
t2.left = TreeNode(1)
t2.right = TreeNode(2)

s = Solution()

print(s.isSubtree(t1, t2))
