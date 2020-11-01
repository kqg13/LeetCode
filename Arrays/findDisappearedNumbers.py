# Array problem 448: Find all numbers disappeared in an array

# Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some
# elements appear twice and others appear once.
#
# Find all the elements of [1, n] inclusive that do not appear in this array.

#  Example: [4, 3, 2, 7, 8, 2, 3, 1] --> [5, 6]

# Also see Array problems #41 (first missing positive) and #442 (find duplicates in array)
from collections import defaultdict


class Solution:
    def findDisappearedDict(self, nums):
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

    # O(N) space
    def findDisappearedNumbersSet(self, nums):
        return list(set(range(1, len(nums) + 1)) - set(nums))

    # O(N) time, O(1) space
    def findDisappearedNumbers(self, nums):
        n, results = len(nums), []
        # Flip
        for i in range(n):
            num = abs(nums[i])
            num -= 1
            if nums[num] > 0:
                nums[num] = -nums[num]
        # Get results by grabbing positive
        for i, ele in enumerate(nums):
            if ele > 0:
                results.append(i + 1)
        return results


s = Solution()
nums1 = [4, 3, 2, 7, 8, 2, 3, 1]
print(s.findDisappearedNumbers(nums1))
