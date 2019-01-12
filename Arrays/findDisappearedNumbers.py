# Easy problem 448: Find all numbers disappeared in an array

# Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some
# elements appear twice and others appear once.
#
# Find all the elements of [1, n] inclusive that do not appear in this array.

from collections import defaultdict


class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        num_count = defaultdict(int)

        for num in nums:
            num_count[num] += 1

        disappeared = []

        for num in range(1, len(nums) + 1):
            if num not in num_count:
                disappeared.append(num)

        return disappeared

    # O(1) space
    def findDisappearedNumbersOptimal(self, nums):
        return list(set(range(1, len(nums) + 1)) - set(nums))
