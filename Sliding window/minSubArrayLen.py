# 209: Minimum Size Subarray Sum
# https://leetcode.com/problems/minimum-size-subarray-sum/

class Solution:
    def minSubArrayLen(self, target, nums) -> int:
        n = len(nums)
        l = curr_sum = 0
        constraint = 10 ** 9
        curr_length = result = constraint
        for r in range(n):
            curr_sum += nums[r]
            while curr_sum >= target:
                curr_length = r - l + 1
                result = min(curr_length, result)
                curr_sum -= nums[l]
                l += 1

        return 0 if result == constraint else result


s = Solution()
target1, nums1 = 7, [2, 3, 1, 2, 4, 3]  # Expected: 2
target2, nums2 = 4, [1, 4, 4]  # Expected: 1
target3, nums3 = 11, [1, 1, 1, 1, 1, 1, 1, 1]  # Expected: 0
target4, nums4 = 11, [1, 2, 3, 4, 5]  # Expected: 3
print(s.minSubArrayLen(target1, nums1))
print(s.minSubArrayLen(target2, nums2))
print(s.minSubArrayLen(target3, nums3))
print(s.minSubArrayLen(target4, nums4))
