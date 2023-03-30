# DP problem 198: House Robber

# You are a professional robber planning to rob houses along a street. Each
# house has a certain amount of money stashed, the only constraint stopping
# you from robbing each of them is that adjacent houses have security system
# connected and it will automatically contact the police if 2 adjacent houses
# were broken into on the same night. Given a list of non-negative integers
# representing the amount of money of each house, determine the max amount of
# money you can rob tonight w/o alerting police.

# Example 1: Input: [1, 2, 3, 1] --> Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
#              Total amount you can rob = 1 + 3 = 4.

# Example 2: Input: [2, 7, 9, 3, 1] --> Output: 12
# Explanation: Rob house 1, rob house 3 and rob house 5 (money = 1).
#              Total amount you can rob = 2 + 9 + 1 = 12.


class Solution:
    def robEli(self, nums) -> int:
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        results = [0] * (len(nums) + 1)
        results[1] = nums[0]
        for i in range(2, len(nums) + 1):
            results[i] = max(results[i - 2] + nums[i - 1], results[i - 1])
        return results[-1]

    def rob(self, nums):
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)

        results = [0] * len(nums)
        results[0] = nums[0]
        results[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            results[i] = max(results[i - 2] + nums[i], results[i - 1])
        return results[-1]

    def rob2(self, nums):
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)

        results = [0] * len(nums)
        results[0] = max(nums[0], nums[-1])
        results[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            results[i] = max(results[i - 2] + nums[i], results[i - 1])
        return results[-1]

    def rob_recursive(self, nums):
        if not nums:
            return 0
        if len(nums) == 1 or len(nums) == 2:
            return max(nums)
        result = self.rob_recursive_helper(nums, 0)
        return result

    def rob_recursive_helper(self, nums, i):
        if i >= len(nums):
            return 0
        r1 = self.rob_recursive_helper(nums, i + 2) + nums[i]
        r2 = self.rob_recursive_helper(nums, i + 1)
        return max(r1, r2)


s = Solution()
nums1 = [1, 2, 3, 1]
nums2 = [2, 7, 9, 3, 1]
      # [2, 7, 11, 11, 12]
      # [1, 7, 10, 10, 11]
nums3 = [100, 1, 1, 100]
print(s.rob_recursive(nums3))
nums4 = [2, 3, 2]

print(s.rob2(nums3))
