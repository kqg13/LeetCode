# 560: Subarray Sum Equals K
# https://leetcode.com/problems/subarray-sum-equals-k/description/


from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count, n = 0, len(nums)

        for i in range(n):
            sum_result = 0
            for j in range(i, n):
                sum_result += nums[j]
                if sum_result == k:
                    count += 1

        return count


s = Solution()
nums1, k1 = [1, 1, 1], 2
nums2, k2 = [1, 2, 3], 3
