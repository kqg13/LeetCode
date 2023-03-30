# 486: Predict the Winner
# https://leetcode.com/problems/predict-the-winner/


class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        balance = self.PredictTheWinnerHelper(nums, 1, 0)
        return balance >= 0

    # first solution
    def PredictTheWinnerHelperRecursive(self, nums, player, balance):
        if not nums: return balance
        sign = 1 if player == 1 else -1
        if len(nums) == 1:
            return balance + (sign * nums[0])
        # overall balance
        balance_first = balance + (sign * nums[0])
        balance_last = balance + (sign * nums[-1])
        if sign == 1:
            take_first = self.PredictTheWinnerHelper(nums[1:], 2, balance_first)
            take_last = self.PredictTheWinnerHelper(nums[:-1], 2, balance_last)
            return max(take_first, take_last)
        else:
            take_first = self.PredictTheWinnerHelper(nums[1:], 1, balance_first)
            take_last = self.PredictTheWinnerHelper(nums[:-1], 1, balance_last)
            return min(take_first, take_last)

    def PredictTheWinnerHelper(self, nums, sign, balance):
        if not nums: return balance
        if len(nums) == 1:
            return balance + (sign * nums[0])
        # overall balance
        balance_first = balance + (sign * nums[0])
        balance_last = balance + (sign * nums[-1])
        take_first = self.PredictTheWinnerHelper(nums[1:], -sign, balance_first)
        take_last = self.PredictTheWinnerHelper(nums[:-1], -sign, balance_last)
        if sign * take_first > sign * take_last:
            return take_first
        return take_last

    def PredictTheWinnerDP(self, nums) -> bool:
        n = len(nums)
        dp = [[0] * n for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                dp[i][j] = max(nums[i] - dp[i + 1][j], nums[j] - dp[i][j - 1])
        return dp[0][n - 1] >= 0


nums1 = [1, 5, 2]  # --> false
nums2 = [1, 5, 233, 7]  # --> true
nums3 = [3, 9, 1, 2]
nums4 = [1, 5, 8, 4]
s = Solution()
print(s.PredictTheWinnerDP(nums4))
