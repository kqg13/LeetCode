# LeetCode 55: Jump Game

# Given an array of non-negative ints nums, you are initially positioned at the first index of the array.
# Each element in the array represents your maximum jump length at that position.
# Determine if you are able to reach the last index.

# Examples:
# nums1 = [2, 3, 1, 1, 4] --> True
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
# nums2 = [3, 2, 1, 0, 4] --> False
# Explanation: You will always arrive at index 3 no matter what. Its max jump length is 0,
# which makes it impossible to reach the last index.


class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        pass


nums1 = [2, 3, 1, 1, 4]
nums2 = [3, 2, 1, 0, 4]
s = Solution()
print(s.canJump(nums1))
print(s.canJump(nums2))