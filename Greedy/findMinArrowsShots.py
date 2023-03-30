# 452: Minimum Number of Arrows to Burst Balloons

# There are some spherical balloons spread in 2D space.
# For each balloon, provided input is the start and end coordinates of the horizontal diameter.
# Since it's horizontal, y-coordinates don't matter, and hence the x-coordinates of
# start and end of the diameter suffice. The start is always smaller than end.
#
# An arrow can be shot up exactly vertically from different points along x-axis.
# A balloon with x-start & x-end bursts by an arrow shot at x if x-start ≤ x ≤ x-end.
# There is no limit to the # of arrows that can be shot. An arrow once shot keeps traveling up infinitely.
#
# Given an array points where points[i] = [x-start, x-end], return the min # of arrows that
# must be shot to burst all balloons.


# Examples:
# points1 = [[10, 16], [2, 8], [1, 6], [7, 12]] ---> 2
# Explanation: One way is to shoot one arrow for example at x = 6
# (bursting the balloons [2,8] and [1,6]) and another arrow at x = 11 (bursting the other 2 balloons)
# points2 = [[1, 2], [3, 4], [5, 6], [7, 8]] ---> 4
# points3 = [[1, 2], [2, 3], [3, 4], [4, 5]] --> 2

class Solution:
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        sorted_points = sorted(points, key=lambda b: b[0])
        currentMin = sorted_points[0][1]
        numArrows = 1
        for i in range(1, len(sorted_points)):
            if currentMin < sorted_points[i][0]:
                currentMin = sorted_points[i][1]
                numArrows += 1
            else:
                currentMin = min(currentMin, sorted_points[i][1])
        return numArrows


s = Solution()
points1 = [[10, 16], [2, 8], [1, 6], [7, 12]]
points2 = [[1, 2], [3, 4], [5, 6], [7, 8]]
points3 = [[1, 2], [2, 3], [3, 4], [4, 5]]
points4 = [[1, 6], [2, 5], [3, 4], [10, 11]]
print(s.findMinArrowShots(points1))
print(s.findMinArrowShots(points2))
print(s.findMinArrowShots(points3))
print(s.findMinArrowShots(points4))
