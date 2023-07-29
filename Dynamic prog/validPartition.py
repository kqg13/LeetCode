# 2369: Check if There is a Valid Partition for the Array
# https://leetcode.com/problems/check-if-there-is-a-valid-partition-for-the-array/

class Solution:
    def validPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        dp = self.createDpArray(n)
        nums = [-1, -1] + nums
        for i in range(3, n + 2):
            case1 = dp[i - 2] and (nums[i - 1] == nums[i])
            case2 = dp[i - 3] and (nums[i - 2] == nums[i - 1] == nums[i])
            case3 = dp[i - 3] and (nums[i - 2] + 2 == nums[i - 1] + 1 == nums[i])
            dp[i] = case1 or case2 or case3
        return dp[-1]

    def createDpArray(self, n):
        dp = [False] * (n + 2)
        # Pad the first two as True, so we don't fail in the first 2 elements
        dp[0] = dp[1] = True
        return dp


s = Solution()
nums1 = [4, 4, 4, 5, 6]  # Expected: True
nums2 = [1, 1, 1, 2]  # Expected: False
nums3 = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 1, 1, 1, 5, 5, 5, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8]
