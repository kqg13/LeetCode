# 303. Range Sum Query - Immutable

# Given an int array nums, handle multiple queries of the following type:
#
# Calc the sum of the elements of nums between indices left and right inclusive where left <= right.
# Implement the NumArray class:
#
# NumArray(int[] nums) Initializes the object with the integer array nums.
# int sumRange(int left, int right) Returns the sum of the elements of nums b/w indices left and right
# inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).

from itertools import accumulate


# Caching: O(N), Query: O(1)
class NumArray:
    def __init__(self, nums):
        self.sums = list(accumulate(nums))

    def sumRange(self, left: int, right: int) -> int:
        left_val = 0
        if left != 0:
            left_val = self.sums[left - 1]
        return self.sums[right] - left_val


# Your NumArray object will be instantiated and called as such:
nums1 = [-2, 0, 3, -5, 2, -1]
obj = NumArray(nums1)
param_1 = obj.sumRange(0, 1)
print(param_1)
