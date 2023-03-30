# Easy array problem 1: Two Sum

# Given an array of integers, return indices of the two numbers such that they
# add up to a specific target.
# You may assume that each input would have exactly one solution, and you may
# not use the same element twice.

# Given nums = [2, 7, 11, 15], target = 9,
# Because nums[0] + nums[1] = 2 + 7 = 9, return [0, 1].


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i in range(0, len(nums) - 1):
            if nums[i] not in d: d[nums[i]] = list(nums[i+1::])

        for key, values in d.items():
            for val in values:
                if key + val == target:
                    num1, num2 = key, val
        output = []

        for i, num in enumerate(nums):
            if num == num1 or num == num2: output.append(i)

        return output

    # O(N) time and O(N) space
    def twoSumBetter(self, nums, target):
        num_indices = {}  # Maps nums[i] to i

        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_indices:
                return [num_indices[complement], i]
            num_indices[num] = i

        return [-1, -1]
