# 3169: Count Days without Meetings
# https://leetcode.com/problems/count-days-without-meetings/description/

from typing import List


class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        sorted_meetings = sorted(meetings, key=lambda x: x[0])
        result = sorted_meetings[0][0] - 1
        last_day = sorted_meetings[0][1]

        for start, end in sorted_meetings[1:]:
            if start > last_day:
                result += start - last_day - 1
            last_day = max(last_day, end)
        # Excess
        result += days - last_day
        return result


s = Solution()
days1, meetings1 = 10, [[5, 7], [1, 3], [9, 10]] # Expected: 2
days2, meetings2 = 5, [[2, 4], [1, 3]]  # Expected: 1
days3, meetings3 = 6, [[1, 6]]  # Expected: 0
