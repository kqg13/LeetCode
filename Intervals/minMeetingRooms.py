# Medium Interval Problem 253: Meeting Rooms II

# Given an array of meeting time intervals consisting of start and end times
# [[s1, e1], [s2, e2], ...] (si < ei), find the min # of conference rooms required.

# Examples:
# Input: [[0, 30],[5, 10],[15, 20]] ---> 2
# Input: [[7, 10], [2, 4]] --> 1

import heapq


class Solution:
    def minMeetingRooms(self, intervals) -> int:
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if not intervals: return 0
        intervals_sorted = sorted(intervals, key=lambda x: x[0])
        count, conf_rooms = 0, []

        # Push first interval
        heapq.heappush(conf_rooms, intervals_sorted[0][1])
        count += 1

        for interval in intervals_sorted[1:]:
            # overlap
            if interval[0] < conf_rooms[0]:
                heapq.heappush(conf_rooms, interval[1])
                count += 1
            else:
                heapq.heappushpop(conf_rooms, interval[1])
        return count


s = Solution()
intervals1 = [[0, 30], [5, 10], [15, 20]]
intervals2 = [[7, 10], [2, 4]]
intervals3 = [[1, 4], [2, 6], [5, 7]]

print(s.minMeetingRooms(intervals1))
print(s.minMeetingRooms(intervals2))
print(s.minMeetingRooms(intervals3))
