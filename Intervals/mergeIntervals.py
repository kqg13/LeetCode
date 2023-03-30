# Medium Interval Problem 56: Merge intervals

# Given a collection of intervals, merge all overlapping intervals.
# to remove to make the rest of the intervals non-overlapping.
#
# Example 1: Input: [[1, 3], [2, 6], [8, 10], [15,18]]
# Output: [[1,6], [8, 10], [15, 18]]
#
# Example 2: Input: [[1, 4], [4, 5]]
# Output: [1, 5]


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals: return []
        sorted_intervals = sorted(intervals, key=lambda x: x[0])
        current, merged = sorted_intervals[0], []
        for interval in sorted_intervals[1:]:
            overlap = current[1] >= interval[0]
            if overlap:
                current[1] = max(current[1], interval[1])
            else:
                merged.append(current)
                current = interval
        merged.append(current)
        return merged


s = Solution()
l1 = [[1, 3], [2, 6], [8, 10], [15,18]]
l2 = [[1, 4], [4, 5]]
l3 = [[3, 8], [9, 20], [17, 19], [19, 25], [24, 25]]
l4 = [[0, 30], [5, 10], [15, 20]]
print(s.merge(l4))
