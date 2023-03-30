# 849: Maximize Distance to Closest Person
# https://leetcode.com/problems/maximize-distance-to-closest-person/


class Solution:
    def maxDistToClosest(self, seats) -> int:
        n = len(seats)
        left_to_right, right_to_left = [float('inf')] * n, [float('inf')] * n
        # left-to-right
        recent_occ_seat = -1
        for i in range(n):
            if seats[i] == 1:
                recent_occ_seat = i
                left_to_right[i] = 0
            else:
                if recent_occ_seat == - 1:
                    continue
                left_to_right[i] = abs(i - recent_occ_seat)
        # right-to-left
        recent_occ_seat = -1
        for i in range(n - 1, -1, -1):
            if seats[i] == 1:
                recent_occ_seat = i
                right_to_left[i] = 0
            else:
                if recent_occ_seat == - 1:
                    continue
                right_to_left[i] = abs(i - recent_occ_seat)
        max_dist = int(max([min(a, b) for a, b in zip(left_to_right, right_to_left)]))
        return max_dist


s = Solution()
seats1 = [1, 0, 0, 0, 1, 0, 1]  # 2
seats2 = [0, 1]  # 1
seats3 = [1, 0, 0, 0]
print(s.maxDistToClosest(seats3))
