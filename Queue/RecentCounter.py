# Easy queue problem 933: Number of Recent Calls

# Write a class RecentCounter to count recent requests.
# It has only one method: ping(int t), where t represents some time in ms.
# Return the # of pings that have been made from 3000 ms ago until now.
# Any ping with time in [t - 3000, t] will count, including the current ping.

# It is guaranteed that every call to ping uses a strictly larger value
# of t than before.

# Example:
# Input: inputs = ["RecentCounter", "ping", "ping", "ping", "ping"]
# inputs = [ [],[1],[100],[3001],[3002] ]
# Output: [null, 1, 2, 3, 3]

from collections import deque


class RecentCounter:

    def __init__(self):
        self.d = deque()

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.d.append(t)
        while self.d[0] < t - 3000:
            self.d.popleft()
        return len(self.d)
