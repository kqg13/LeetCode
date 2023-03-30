# Bit manipulation #268: Missing Number

# Given an array nums containing n distinct nums in the range [0, n], return the
# only number in the range missing from the array.

# Examples:
# nums1 = [3, 0, 1] --> 2
# nums2 = [0, 1] --> 2
# nums3 = [9, 6, 4, 2, 3, 5, 7, 0, 1] --> 8


class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        # initialize missing
        missing = n
        for i, num in enumerate(nums):
            missing ^= num ^ i
        return missing


s = Solution()
nums1 = [3, 0, 1]
nums2 = [0, 1]
nums3 = [9, 6, 4, 2, 3, 5, 7, 0, 1]
print(s.missingNumber(nums1))
print(s.missingNumber(nums2))
print(s.missingNumber(nums3))
