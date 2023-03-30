# DP problem 256: Paint House

# There are a row of n houses, each house can be painted with one of the
# 3 colors: red, blue or green. The cost of painting each house with a certain
# color is different. You have to paint all the houses such that no 2 adjacent
# houses have the same color.
#
# The cost of painting each house with a certain color is represented by
# a n x 3 cost matrix. For example, costs[0][0] is the cost of painting house
# 0 with color red; costs[1][2] is the cost of painting house 1 with color
# green, and so on. Find the minimum cost to paint all houses.

# Input: [[17, 2, 17], [16, 16, 5], [14, 3, 19]], Output: 10
# Explanation: Paint house 0 into blue, paint house 1 into green,
#              paint house 2 into blue.
#              Minimum cost: 2 + 5 + 3 = 10.


class Solution:
    def minCost(self, costs):
        """
        :param costs: List[List[int]]
        :return: int
        """
        costs_len = len(costs)
        if costs_len == 0:
            return 0

        for i in range(1, costs_len):
            costs[i][0] += min(costs[i - 1][1], costs[i - 1][2])
            costs[i][1] += min(costs[i - 1][0], costs[i - 1][2])
            costs[i][2] += min(costs[i - 1][0], costs[i - 1][1])

        return min(min(costs[costs_len - 1][0], costs[costs_len - 1][1]),
                   costs[costs_len - 1][2])


# Test
arr = [
    [3, 5, 3],
    [6, 17, 6],
    [7, 13, 18],
    [9, 10, 18]
    ]
s = Solution()
print(s.minCost(arr))  # Expected: 26
