# LeetCode 654: Maximum Binary Tree

# You are given an int array nums with no duplicates. A maximum binary tree can
# be built recursively from nums using the following algorithm:
#
# Create a root node whose value is the maximum value in nums.
# Recursively build left subtree on the subarray prefix to the left of the max value.
# Recursively build right subtree on the subarray suffix to the right of the max value.
# Return the max binary tree built from nums.


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        if len(nums) == 1:
            leaf = TreeNode(nums[0])
            return leaf
        max_val = max(nums)
        max_idx = nums.index(max_val)
        root = TreeNode(max_val)
        root.left = self.constructMaximumBinaryTree(nums[0:max_idx])
        root.right = self.constructMaximumBinaryTree(nums[max_idx + 1:len(nums)])
        return root


s = Solution()
nums1 = [3, 2, 1, 6, 0, 5]
print(s.constructMaximumBinaryTree(nums1))
