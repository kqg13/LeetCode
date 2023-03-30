# Medium Interval Problem 253: Meeting Rooms II

# Given an array of meeting time intervals consisting of start and end times
# [[s1, e1], [s2, e2], ...] (si < ei), find the min # of conference rooms required.

# Examples:
# Input: [[0, 30],[5, 10],[15, 20]] ---> 2
# Input: [[7, 10], [2, 4]] --> 1

import heapq


class Solution:
    def minMeetingRoomsReview(self, intervals):
        sorted_intervals = sorted(intervals, key=lambda t: t[0])
        count, rooms = 1, list()
        heapq.heappush(rooms, sorted_intervals[0][1])
        for interval in sorted_intervals[1:]:
            if interval[0] < rooms[0]:
                heapq.heappush(rooms, interval[1])
                count += 1
            else:
                heapq.heappushpop(rooms, interval[1])  # this still has to be scheduled
        return count

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
intervals4 = [[9, 10], [4, 9], [4, 17]]
intervals5 = [[13, 15], [1, 13]]

print(s.minMeetingRoomsReview(intervals1), s.minMeetingRooms(intervals1))
print(s.minMeetingRoomsReview(intervals2), s.minMeetingRooms(intervals2))
print(s.minMeetingRoomsReview(intervals3), s.minMeetingRooms(intervals3))
print(s.minMeetingRoomsReview(intervals4), s.minMeetingRooms(intervals4))
print(s.minMeetingRoomsReview(intervals5), s.minMeetingRooms(intervals5))
