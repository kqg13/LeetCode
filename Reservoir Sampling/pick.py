# 398: Random Pick Index
# https://leetcode.com/problems/random-pick-index/?envType=problem-list-v2&envId=reservoir-sampling

import random


class Solution:
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        count = 0
        index = -1
        for i, num in enumerate(self.nums):
            if num == target:
                count += 1
                if self.doPick(count):
                    index = i
        return index

    def doPick(self, x):
        rnd = random.randint(1, x)
        return rnd == 1


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
nums1 = [1, 2, 3, 3, 3]
obj = Solution(nums1)
target = 3
print(obj.pick(target))
print(obj.pick(target))
print(obj.pick(target))
