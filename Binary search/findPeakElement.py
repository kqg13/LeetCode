# LeetCode problem 162: Find Peak Element

# A peak element is an element that is strictly greater than its neighbors.
# Given an int array nums, find a peak element, and return its index.
# If the array contains multiple peaks, return the index to any of the peaks.

# nums1 = [1, 2, 3, 1] ---> 2
# nums2 = [1, 2, 1, 3, 5, 6, 4] ---> 5


class Solution:
    def findPeakElementLinear(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numslen = len(nums) - 1
        for i in range(numslen):
            if nums[i] > nums[i + 1]:
                return i
        return numslen


nums1 = [1, 2, 3, 1]
nums2 = [1, 2, 1, 3, 5, 6, 4]
s = Solution()
print(s.findPeakElementLinear(nums1))
print(s.findPeakElementLinear(nums2))
