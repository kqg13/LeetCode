# Medium DP problem 322: Coin Change
# https://leetcode.com/problems/coin-change/


# Time: O(N * coins), Space: O(N) where N is amount
class Solution(object):
    def coinChangeRecursive(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        self.best = float('inf')
        self.coins = coins
        self.coinChangeHelper(amount, 0)
        if self.best == float('inf'):
            return -1
        return self.best

    def coinChangeHelper(self, amount, depth):
        if amount == 0:
            self.best = min(self.best, depth)
            return
        for coin in self.coins:
            if amount - coin < 0:
                continue
            self.coinChangeHelper(amount - coin, depth + 1)

    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0: return 0
        if not coins: return -1
        results = [-1] * (amount + 1)
        results[0] = 0
        for s in range(1, amount + 1):
            subprobs = list()
            for coin in coins:
                sub_s = s - coin
                if sub_s < 0 or results[sub_s] == -1:
                    continue
                subprobs.append(results[sub_s])
            if subprobs:
                results[s] = min(subprobs) + 1
        return results[-1]

    def coinChangeCleaner(self, coins, amount):
        if len(coins) == 0 or amount == 0: return 0

        results = [float('inf')] * (amount + 1)
        results[0] = 0

        for amt in range(1, amount + 1):
            for coin in coins:
                if amt >= coin:
                    results[amt] = min(results[amt], 1 + results[amt - coin])

        return results[-1] if results[-1] != float('inf') else -1


coins1, target1 = [1, 2, 5], 11
coins2, target2 = [2], 3
coins3, target3 = [1], 1
s = Solution()
