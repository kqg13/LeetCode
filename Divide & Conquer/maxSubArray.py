# LeetCode Divide & conquer problem 53: Maximum Subarray

# Given an integer array nums, find the contiguous subarray
# (containing at least one number) which has the largest sum and return its
# sum.

# Example:
# Input: [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6


# Time: O(NlogN), Space: O(logN)
class Solution:
    def maxSubArray(self, nums) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        self.nums = nums
        result = self.maxSubArrayDivideConquer(0, len(self.nums) - 1)
        return result

    def maxSubArrayDivideConquer(self, low, high):
        if low == high:
            return self.nums[low]
        mid = (low + high) // 2
        left_sum = self.maxSubArrayDivideConquer(low, mid)  # mid element always falls on left side
        right_sum = self.maxSubArrayDivideConquer(mid + 1, high)
        cross_sum = self.calcCrossSum(low, high, mid)
        return max(left_sum, right_sum, cross_sum)

    def calcCrossSum(self, low, high, mid):
        lsum, rsum = 0, 0
        lmax, rmax = 0, 0
        for i in range(mid - 1, low - 1, -1):
            lsum += self.nums[i]
            lmax = max(lsum, lmax)
        for i in range(mid + 1, high + 1):
            rsum += self.nums[i]
            rmax = max(rsum, rmax)
        cross_sum = lmax + rmax + self.nums[mid]
        return cross_sum


s = Solution()
nums1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(s.maxSubArray(nums1))
