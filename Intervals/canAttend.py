# Easy Interval Problem 252: Meeting Rooms

# Given an array of meeting time intervals consisting of start and end times
# [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.

# Examples:
# Input: [[0, 30], [5, 10], [15, 20]] --> false
# Input: [[7, 10], [2, 4]] --> true


class Solution:
    def canAttendMeetings(self, intervals):
        intervals_new = sorted(intervals, key=lambda x: x[0])
        for i in range(1, len(intervals_new)):
            if intervals_new[i][0] < intervals_new[i-1][1]:
                return False
        return True
