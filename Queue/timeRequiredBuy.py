# 2073: Time Needed to Buy Tickets
# https://leetcode.com/problems/time-needed-to-buy-tickets/

class Solution:
    def timeRequiredToBuy(self, tickets, k):
        """
        tickets: List[int]
        k: int
        return: int
        """
        v = tickets[k]

        # Everything before k
        k_before = [min(v, tickets[i]) for i in range(k)]
        # Everything after k
        k_after = [min(v - 1, tickets[i]) for i in range(k + 1, len(tickets))]

        result = sum(k_before) + v + sum(k_after)
        return result


s = Solution()
tickets1, k1 = [2, 3, 2], 2  # Expected: 6
tickets2, k2 = [5, 1, 1, 1], 0  # Expected: 8
