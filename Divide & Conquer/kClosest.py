# LeetCode problem 973: K Closest Points to Origin

# We have a list of points on the plane.  Find the K closest points to the
# origin (0, 0).
#
# Here, the distance between two points on a plane is the Euclidean distance.
#
# You may return the answer in any order.  The answer is guaranteed to be
# unique except for the order that it is in.

# Input: points1, K = [[1, 3], [-2, 2]], K = 1 ---> [[-2, 2]]
# Input: points2, K = [[3, 3], [5, -1], [-2, 4]], K = 2 --->  [[3, 3], [-2, 4]]


class Solution:
    # O(NlogN)
    def kClosestSorting(self, points, K):
        sorted_points = sorted(points, key=lambda p: self.calcDistance(p))
        return sorted_points[:K]

    def calcDistance(self, point):
        return point[0] ** 2 + point[1] ** 2

    def partition(self, points, low, high):
        divider, pivot = low, high
        for i in range(low, high):
            if points[i][0] < points[pivot][0]:
                points[i], points[divider] = points[divider], points[i]
                divider += 1
        points[divider], points[pivot] = points[pivot], points[divider]
        return divider

    # O(N) we take advantage that points can be returned in any order
    def quickSelect(self, points, low, high, K):
        if low < high:
            p = self.partition(points, low, high)
            if p == K:
                return
            elif p < K:
                self.quickSelect(points, p + 1, high, K)
            else:
                self.quickSelect(points, low, p - 1, K)

    def kClosest(self, points: 'list[list[int]]', K: int):
        points = [(self.calcDistance(p), p) for p in points]
        self.quickSelect(points, 0, len(points) - 1, K)
        return [p for _, p in points[:K]]


s = Solution()
points1, k1 = [[1, 3], [-2, 2]], 1
points2, k2 = [[3, 3], [5, -1], [-2, 4]], 2
points3, k3 = [[-2, 10], [-4, -8], [10, 7], [-4, -7]], 3
points5, k5 = [[100, -16], [-31, 45], [80, -47], [41, 59], [-59, -34], [-34, -76], [-5, -77], [35, 40], [58, -30],
               [31, -96], [40, 14], [-25, 50], [37, -38], [-54, -31]], 8

# print(s.kClosest(points1, k1))
# print(s.kClosest(points2, k2))
print(s.kClosest(points5, k5))
print(s.kClosestSorting(points5, k5))
print(points5[:3])

