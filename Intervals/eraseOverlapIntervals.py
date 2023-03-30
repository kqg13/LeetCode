# Medium Interval Problem 435: Non-overlapping intervals

# Given a collection of intervals, find the min number of intervals you need
# to remove to make the rest of the intervals non-overlapping.
#
# Example 1: Input: [[1, 2], [2, 3], [3, 4], [1, 3]], Output: 1
# Explanation: [1,3] can be removed and the rest of intervals are non-overlapping
#
# Example 2: Input: [[1, 2], [1, 2], [1, 2]], Output: 2
# Explanation: You need to remove two [1,2] to make the rest of intervals non-overlapping
#
# Example 3: Input: [[1, 2], [2, 3]], Output: 0
# Explanation: You don't need to remove any of the intervals since they're already non-overlapping


# Greedy approach time: O(NlogN)
class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if len(intervals) == 0 or len(intervals) == 1:
            return 0
        intervals_sorted = sorted(intervals, key=lambda x: x[0])
        count, prev_interval = 0, 0
        for i in range(1, len(intervals_sorted)):
            if intervals_sorted[prev_interval][1] > intervals_sorted[i][0]:
                if intervals_sorted[prev_interval][1] > intervals_sorted[i][1]:
                    prev_interval = i
                count += 1
            else:
                prev_interval = i
        return count
