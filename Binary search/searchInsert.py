# Easy binary search 35: Search Insert Position

# Given a sorted array and a target value, return the index if the target is
# found. If not, return index where it would be if it were inserted in order.
# You may assume no duplicates in the array.


from bisect import bisect_left

# Example 1: Input: [1, 3, 5, 6], 5, Output: 2
# Example 2:
# Input: [1, 3, 5, 6], 2, Output: 1


class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return bisect_left(nums, target)
