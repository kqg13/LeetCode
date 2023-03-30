# 108: Convert Sorted Array to Binary Search Tree

# Given an int array nums where the elements are sorted in asc order, convert it to a height-balanced BST.
#
# A height-balanced binary tree is a binary tree in which the depth of the 2 subtrees
# of every node never differs by more than 1.


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        self.curr_idx = 0
        root = self.sortedArrayToBSThelper(nums, 0, len(nums) - 1)
        return root

    def sortedArrayToBSThelper(self, nums, low, high):
        # Base case
        if low > high:
            return None

        mid = (low + high) // 2
        l = self.sortedArrayToBSThelper(nums, low, mid - 1)
        root = TreeNode(nums[self.curr_idx])
        self.curr_idx += 1
        r = self.sortedArrayToBSThelper(nums, mid + 1, high)

        root.left = l
        root.right = r
        return root


nums1 = [-10, -3, 0, 5, 9]
nums2 = [1, 3]
s = Solution()
print(s.sortedArrayToBST(nums1))
