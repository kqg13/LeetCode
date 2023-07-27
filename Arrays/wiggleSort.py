# 280: Wiggle Sort
# https://leetcode.com/problems/wiggle-sort/

class Solution:
    def wiggleSort(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums) - 1):
            prev_num = nums[i]
            next_num = nums[i + 1]

            if (i % 2 == 0 and prev_num > next_num) or (i % 2 == 1 and prev_num < next_num):
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
