# LeetCode 113: Path Sum II

# Given the root of a binary tree and an int targetSum, return all root-to-leaf paths
# where each path's sum equals targetSum.  A leaf is a node with no children.

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        self.results = []
        self.targetSum = targetSum
        self.pathSumHelperIncorrect(root, [], 0)
        return self.results

    def pathSumHelperIncorrect(self, root, currentPath, runningSum):
        runningSum += root.val
        currentPath.append(root.val)
        print("current: ", currentPath)
        if root.left is None and root.right is None:
            if runningSum == self.targetSum:
                self.results.append(currentPath.copy())
            # Backtrack
            currentPath.pop()
            # runningSum -= root.val
            return
        if root.left:
            self.pathSumHelperIncorrect(root.left, currentPath, runningSum)
            currentPath.pop()
        if root.right:
            self.pathSumHelperIncorrect(root.right, currentPath, runningSum)
            currentPath.pop()

    def pathSumHelperCorrect(self, root, currentPath, runningSum):
        runningSum += root.val
        currentPath.append(root.val)
        print("current: ", currentPath)
        if root.left is None and root.right is None:
            if runningSum == self.targetSum:
                self.results.append(currentPath.copy())
        if root.left:
            self.pathSumHelperCorrect(root.left, currentPath, runningSum)
        if root.right:
            self.pathSumHelperCorrect(root.right, currentPath, runningSum)
        # Backtrack
        currentPath.pop()


t = TreeNode(5)
# Left subtree
t.left = TreeNode(4)
t.left.left = TreeNode(11)
t.left.left.left = TreeNode(7)
t.left.left.right = TreeNode(2)
# Right subtree
t.right = TreeNode(8)
t.right.left = TreeNode(13)
t.right.right = TreeNode(4)
t.right.right.left = TreeNode(5)
t.right.right.right = TreeNode(1)
s = Solution()
print(s.pathSum(t, 22))

