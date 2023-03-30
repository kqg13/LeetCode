# Medium Tree Problem 814: Binary Tree Pruning

# Given an integer array nums, find the contiguous subarray within an array
# (containing at least one number) which has the largest product.


class Solution:
    def maxProduct(self, nums) -> int:
        max_prod, min_prod, result = nums[0], nums[0], nums[0]
        for num in nums[1:]:
            npmax, npmin = num * max_prod, num * min_prod
            max_prod = max(num, npmax, npmin)
            min_prod = min(num, npmax, npmin)
            result = max(result, max_prod)
        return result


s = Solution()
nums1 = [2, -2, 4, 3, -2, 2, -3, 2]
s.maxProduct(nums1)
