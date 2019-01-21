# Easy binary search problem 704: Binary Search

# Given a sorted (in ascending order) integer array nums of n elements and a
# target value, write a function to search target in nums. If target exists,
# then return its index, otherwise return -1.

from bisect import bisect_left


class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        def search_rec(low, high, nums, target):
            if high >= low:
                mid = (low + high) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    return search_rec(mid + 1, high, nums, target)
                else:
                    return search_rec(low, mid - 1, nums, target)
            else:
                return -1

        return search_rec(0, len(nums) - 1, nums, target)

    # Using bisect module which assumes list is sorted
    def bisect_search(self, nums, target):
        index = bisect_left(nums, target)
        return index if index < len(nums) and nums[index] == target else -1
