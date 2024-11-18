# 718. Maximum Length of Repeated Subarray
# https://leetcode.com/problems/maximum-length-of-repeated-subarray/

class Solution(object):
    def findLength(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        m, n = len(nums1), len(nums2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                increment = 1 if nums1[i] == nums2[j] else 0
                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j]) + increment
        return dp[-1][-1]


s = Solution()
nums1, nums2 = [1, 2, 3, 2, 1], [3, 2, 1, 4, 7]
nums3, nums4 = [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]
