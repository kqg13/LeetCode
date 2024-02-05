# 1155: Number of Dice Rolls with Target Sum
# https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/
from functools import cache


class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        self.mod = (10 ** 9) + 7
        count = self.numRollsToTargetHelper(n, k, target, 0, 0)
        return count

    @cache
    def numRollsToTargetHelper(self, n, k, target, dice_num, current_sum):
        if dice_num == n:
            if current_sum == target:
                return 1
            else:
                return 0

        if target - current_sum < 0:
            return 0

        count = 0
        for i in range(1, k + 1):
            count += self.numRollsToTargetHelper(n, k, target, dice_num + 1, current_sum + i)

        return count % self.mod

    def numRollsToTargetDp(self, n: int, k: int, target: int) -> int:
        # self.dp = [[0] * (target + 1)] * (n + 1) # BUG
        self.dp = [[0 for _ in range(target + 1)] for _ in range(n + 1)]  # CORRECT
        self.initializeDp(n, k, target)
        # for row in self.dp: print(row)  # pretty print
        modVal = (10 ** 9) + 7

        for i in range(2, n + 1):
            for j in range(i, target + 1):
                currentTarget = j
                start = max(1, currentTarget - k)
                s = sum(self.dp[i - 1][start:currentTarget]) % modVal
                self.dp[i][j] = s

        return self.dp[n][target] % modVal

    def initializeDp(self, n, k, target):
        # initialize first row
        upper_fill = min(k + 1, target + 1)
        for c in range(1, upper_fill):
            self.dp[1][c] = 1


s = Solution()
n1, k1, target1 = 1, 6, 3  # Expected: 1
n2, k2, target2 = 2, 6, 7  # Expected: 6
n3, k3, target3 = 30, 30, 500  # Expected: 222616187
n4, k4, target4 = 4, 4, 8  # Expected: 31
