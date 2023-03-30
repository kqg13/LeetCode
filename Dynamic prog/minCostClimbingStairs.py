# Easy DP problem 746: Min Cost Climbing Stairs

# On a staircase, the i-th step has some non-negative cost cost[i]
# assigned (0 indexed).
#
# Once you pay the cost, you can either climb one or two steps. You need
# to find minimum cost to reach the top of the floor, and you can either
# start from the step with index 0, or the step with index 1.

# Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1], Output: 6
# Explanation: Cheapest is start on cost[0], and only step on 1s,
# skipping cost[3].


class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :param cost: : List[int]
        :return: int
        """
        for i in range(2, len(cost)):
            cost[i] += min(cost[i - 1], cost[i - 2])
        return min(cost[len(cost) - 1], cost[len(cost) - 2])


# Test
s = Solution()
costs = [10, 15, 20]
# costs = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
print(s.minCostClimbingStairs(costs))
