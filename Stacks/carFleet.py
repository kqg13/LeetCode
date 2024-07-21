# 853: Car Fleet
# https://leetcode.com/problems/car-fleet/
# https://leetcode.com/problems/car-fleet/discuss/5255925/Python-solution-with-intuition
# NeetCode: https://www.youtube.com/watch?v=Pr6T-3yB9RM

class Solution(object):
    # O(NlogN)
    def carFleetWithStack(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        pairs = [[pos, speed] for pos, speed in zip(position, speed)]
        stack = []
        for p, s in sorted(pairs)[::-1]:
            time_to_target = (target - p) / s
            if not stack or time_to_target > stack[-1]:
                stack.append(time_to_target)

        return len(stack)

    # O(NlogN) but stack not necessary
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        pairs = [[pos, speed] for pos, speed in zip(position, speed)]
        fleet_count, current_closest = 0, float('-inf')
        for p, s in sorted(pairs)[::-1]:
            time_to_target = (target - p) / s
            if time_to_target > current_closest:
                fleet_count += 1
                current_closest = time_to_target

        return fleet_count


s = Solution()
target1, position1, speed1 = 12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]  # Expected: 3
target2, position2, speed2 = 10, [13], [3]  # Expected: 1
target3, position3, speed3 = 100, [0, 2, 4], [4, 2, 1]  # Expected: 1
