# Bit manipulation #136: Single Number
#
# Given a non-empty array of ints, every element appears twice except for one.
# Find that single one in linear time without using extra space

# Examples:
# nums1 = [2, 2, 1] --> 1
# nums2 = [4, 1, 2, 1, 2] --> 4
# nums3 = [1] --> 1

from functools import reduce


# Time: O(N), Space: O(1)
# Logic: a XOR b XOR a = b
class Solution:
    def singleNumber(self, nums):
        """
         :type nums: List[int]
         :rtype: int
        """
        return reduce(lambda a, b: a ^ b, nums)


s = Solution()
nums1 = [2, 2, 1]
nums2 = [4, 1, 2, 1, 2]
nums3 = [1]
print(s.singleNumber(nums1))
