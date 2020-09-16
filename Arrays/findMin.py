# Medium Array Problem 153: Find Minimum in Rotated Sorted Array

# Suppose an array sorted in ascending order is rotated at some pivot unknown
# to you beforehand.
# i.e., [0, 1, 2, 4, 5, 6, 7] might become [4, 5, 6, 7, 0, 1, 2].

# Find the minimum element. You may assume no duplicate exists in the array.

# Example 1: Input: [3,4,5,1,2] ---> 1
# Example 2: Input: [4, 5, 6, 7, 0, 1, 2] ---> 0


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first, last = nums[0], nums[len(nums) - 1]
        if len(nums) == 1 or first < last: return first
        for i, num in enumerate(nums[1:], start=1):
            if nums[i] < nums[i - 1]:
                return nums[i]


s = Solution()
nums1 = [4, 5, 6, 7, 0, 1, 2]
nums2 = [3, 4, 5, 1, 2]
print(s.findMin(nums1))
print(s.findMin(nums2))
