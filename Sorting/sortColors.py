# LeetCode Problem 75: Sort Colors

# Given an array nums with n objects colored red, white, or blue, sort them
# in-place so that objects of the same color are adjacent, with the
# colors in the order red, white, and blue.

# We will use the integers 0, 1, and 2 to represent the color R, W, and B respectively.

# Input: nums1 = [2, 0, 2, 1, 1, 0] --> [0, 0, 1, 1, 2, 2]
# Input: nums2 = [2, 0, 1] --> [0, 1, 2]

# Invariants: anything < low are 0s, anything > high are all 2s and anything b/w low and high have not yet been seen


class Solution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        low, mid, high = 0, 0, len(nums) - 1
        while mid <= high:
            if nums[mid] == 2:
                nums[high], nums[mid] = nums[mid], nums[high]
                high -= 1
            elif nums[mid] == 0:
                nums[mid], nums[low] = nums[low], nums[mid]
                low += 1
                mid += 1
            else:
                mid += 1


s = Solution()
nums1 = [2, 0, 2, 1, 1, 0]
nums2 = [2, 0, 1]  # this example will tell you why it's mod <= high (another swap necessary)
nums3 = [0, 1, 2, 0, 1, 2]
