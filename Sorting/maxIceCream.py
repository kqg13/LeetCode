# 1833: Maximum Ice Cream Bars
# https://leetcode.com/problems/maximum-ice-cream-bars/description/?envType=problem-list-v2&envId=counting-sort

from typing import List


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        k, result = max(costs), 0
        costs_mapping = [0] * (k + 1)
        # Populate mapping
        for cost in costs:
            costs_mapping[cost] += 1

        for i, cm in enumerate(costs_mapping):
            if coins < 1 or i > coins:
                break
            # No item for that cost
            if cm == 0:
                continue
            pickup_units = min(coins // i, cm)
            result += pickup_units
            coins -= pickup_units * i
        return result


s = Solution()
costs1, coins1 = [1, 3, 2, 4, 1], 7  # Expected: 4
costs2, coins2 = [10, 6, 8, 7, 7, 8], 5  # Expected: 0
costs3, coins3 = [1, 6, 3, 1, 2, 5], 20  # Expected: 6
s.maxIceCream(costs1, coins1)
s.maxIceCream(costs2, coins2)
s.maxIceCream(costs3, coins3)
