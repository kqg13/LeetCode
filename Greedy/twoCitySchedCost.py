# 1029: Two City Scheduling
# https://leetcode.com/problems/two-city-scheduling

class Solution:
    def twoCitySchedCost(self, costs):
        """
        costs: List[List[int]]
        return: int
        """
        data = self.getCostData(costs)
        n = len(costs) / 2
        A_count, B_count, total_cost = n, n, 0
        for cost_A, cost_B, send_airport, penalty in data:
            if A_count == 0:
                total_cost += cost_B
                continue
            elif B_count == 0:
                total_cost += cost_A
                continue

            if send_airport == 'A':
                A_count -= 1
                total_cost += cost_A
            else:
                B_count -= 1
                total_cost += cost_B

        return total_cost

    def getCostData(self, costs):
        """
        costs: List[List[int]]
        return: List[List[cost_airport_A, cost_airport_B, send_airport, penalty]]
        """
        data = list()
        for cost in costs:
            airport_A = cost[0]
            airport_B = cost[1]
            send_airport = 'A' if airport_B > airport_A else 'B'
            penalty = abs(cost[1] - cost[0])
            data.append([airport_A, airport_B, send_airport, penalty])
        return sorted(data, key=lambda x: x[3], reverse=True)


s = Solution()
costs1 = [[10, 20], [30, 200], [400, 50], [30, 20]]  # Expected: 110
costs2 = [[259, 770], [448, 54], [926, 667], [184, 139], [840, 118], [577, 469]]  # Expected: 1859
costs3 = [
            [515, 563], [451, 713], [537, 709], [343, 819],
            [855, 779], [457, 60], [650, 359], [631, 42]
         ]  # Expected: 3086

print(s.twoCitySchedCost(costs1))
print(s.twoCitySchedCost(costs2))
print(s.twoCitySchedCost(costs3))
