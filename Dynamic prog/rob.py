# Easy DP problem 198: House Robber

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
    def rob(self, nums):
        """"
        :param nums: List[int]
        :return: int
        """
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)

        results = [0] * len(nums)
        results[0], results[1] = nums[0], max(nums[0], nums[1])

        for i in range(2, len(nums)):
            results[i] = max(results[i - 2] + nums[i], results[i - 1])
        return results[-1]


# Test
s = Solution()
n = [2, 7, 9, 3, 1]
print(s.rob(n))
