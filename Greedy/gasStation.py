# 134: Gas Station
# https://leetcode.com/problems/gas-station/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(gas) - sum(cost) < 0:
            return -1

        s, n = -1, len(gas)
        while s < n:
            s += 1
            net = gas[s] - cost[s]
            # Get starting point
            if net < 0:
                continue
            current = (s + 1) % n
            accumulate = net
            while current != s:
                current_net = gas[current] - cost[current]
                accumulate += current_net
                if accumulate < 0:
                    s = current % n
                    break
                current = (current + 1) % n
            if current == s and accumulate >= 0:
                break
        return s

    # Explanation: https://www.youtube.com/watch?v=lJwbPZGo05A
    def canCompleteCircuitClean(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(gas) - sum(cost) < 0:
            return -1

        start, accumulate, n = 0, 0, len(gas)

        for i in range(n):
            accumulate += gas[i] - cost[i]

            if accumulate < 0:
                accumulate = 0
                start = i + 1
        return start


gas1, cost1 = [1, 2, 3, 4, 5], [3, 4, 5, 1, 2]
gas2, cost2 = [2, 3, 4],  [3, 4, 3]
