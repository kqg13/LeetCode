# 121: Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices is None: return 0
        dp = [0] * len(prices)
        current_min = prices[0]
        for i in range(1, len(prices)):
            if prices[i] > current_min:
                dp[i] = max(dp[i - 1], prices[i] - current_min)
            else:
                dp[i] = max(0, dp[i - 1])
            current_min = min(current_min, prices[i])
        return dp[-1]


prices1 = [7, 1, 5, 3, 6, 4]
prices2 = [7, 6, 4, 3, 1]
prices3 = [7, 6, 2, 4, 1, 11]
s = Solution()
print(s.maxProfit(prices1))
print(s.maxProfit(prices2))
print(s.maxProfit(prices3))
