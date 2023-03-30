# Easy DP problem 121: Best Time to Buy & Sell Stock

# Say you have an array for which the ith element is the price of given stock
# on day i. If you were only permitted to complete at most 1 transaction
# (buy one and sell one share of the stock), design an algorithm to
# find the max profit. Note that you cannot sell a stock before you buy one.

# Input: [7, 1, 5, 3, 6, 4] --> Output: 5
# Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.

# Input: [7, 6, 4, 3, 1] --> Output: 0
# In this case, no transaction is done, i.e. max profit = 0.


class Solution:
    def maxProfit(self, prices):
        """
        :param prices: List[int]
        :return: int
        """
        count = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                prices[i] = prices[i] - prices[i - 1]
                prices[i], prices[i - 1] = prices[i - 1], prices[i]
                count += 1
            else:
                prices[i - 1] = 0

        return max(prices) if count > 0 else 0


# Even better solution:
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/discuss/39038/Kadane's-Algorithm-Since-no-one-has-mentioned-about-this-so-far-%3A)-(In-case-if-interviewer-twists-the-input)
