# Easy array problem 973: K Closest Points to Origin

# We have a list of points on the plane.  Find the K closest points to the
# origin (0, 0).
#
# Here, the distance between two points on a plane is the Euclidean distance.
#
# You may return the answer in any order.  The answer is guaranteed to be
# unique except for the order that it is in.

from heapq import heappush, heappushpop, nsmallest


class Solution:
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        points.sort(key=lambda i: i[0]**2 + i[1]**2)
        return points[:K]

    # MAX heap implementation
    # O(n + (n-k * logK))
    def kClosestHeap(self, points, K):

        def calcdistance(point):
            return point[0]**2 + point[1]**2

        heap = []
        # Add first k points
        for i in range(K):  # O(KlogK)
            heappush(heap, (-calcdistance(points[i]), points[i]))

        # Maintain heap invariant and k closest for remaining points
        for i in range(K, len(points)):  # O(n-k)
            heappushpop(heap, (-calcdistance(points[i]), points[i]))  # O(logK)

        # Return k items
        return [point[1] for point in nsmallest(K, heap)]  # O(n)
