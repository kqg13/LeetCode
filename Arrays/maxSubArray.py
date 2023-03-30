# Easy divide & conquer problem 53: Maximum Subarray

# Given an integer array nums, find the contiguous subarray
# (containing at least one number) which has the largest sum and return its
# sum.

# Example:
# Input: [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6


class Solution:
    # This is optimal: O(N)
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(1, len(nums)):
            nums[i] = max(nums[i], nums[i] + nums[i - 1])
        return max(nums)

    # https://discuss.leetcode.com/topic/80136/python-solution-with-detailed-explanation
    def maxSubArrayDivideConquer(self, nums):

        def helper(nums, low, high):
            if low == high:
                return nums[low]

            mid = low + (high - low) // 2

            x_left = helper(nums, low, mid)
            x_right = helper(nums, mid + 1, high)
            lmax, rmax = float('-inf'), float('-inf')
            lsum, rsum = 0, 0

            # Left side
            for i in range(mid - 1, low - 1, -1):
                lsum += nums[i]
                lmax = max(lmax, lsum)
            # Right side
            for i in range(mid + 1, high + 1, 1):
                rsum += nums[i]
                rmax = max(rmax, rsum)

            return max(x_left, x_right, max(0, lmax) + max(0, rmax) + nums[mid])

        return helper(nums, 0, len(nums) - 1)


s = Solution()
arr = [2, -5, 8, 6, -2, 5]
print(s.maxSubArrayDivideConquer(arr))