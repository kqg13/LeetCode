# Medium DP problem 322: Coin Change
# https://leetcode.com/problems/coin-change/


# Time: O(N * coins), Space: O(N) where N is amount
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if len(coins) == 0 or amount == 0: return 0

        results = [float('inf')] * (amount + 1)
        results[0] = 0

        for amt in range(1, amount + 1):
            for coin in coins:
                if amt >= coin:
                    results[amt] = min(results[amt], 1 + results[amt - coin])

        return results[-1] if results[-1] != float('inf') else -1

