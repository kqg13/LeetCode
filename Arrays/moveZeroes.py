# Easy problem 283: Move Zeroes

# Given an array nums, write a function to move all 0's to the end of it while
# maintaining the relative order of the non-zero elements.
# Minimize total # of operations.


class Solution:
    # O(N) but number of operations is suboptimal
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        count = nums.count(0)
        nums[:] = [num for num in nums if num != 0]
        for i in range(count):
            nums.append(0)

    # O(N)
    def moveZeroesOptimal(self, nums):
        pos = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[pos], nums[i] = nums[i], nums[pos]
                pos += 1
