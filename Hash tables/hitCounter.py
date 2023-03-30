# 362: Design Hit Counter
# https://leetcode.com/problems/design-hit-counter/

from collections import deque


class HitCounter:
    def __init__(self):
        self.q = deque([])

    def hit(self, timestamp):
        """
        :param timestamp: int
        :return: None
        """
        self.q.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        """
        :param timestamp: int
        :return: int
        """
        while self.q:
            if self.q[0] + 300 <= timestamp:
                self.q.popleft()
            else:
                break
        return len(self.q)


hc = HitCounter()
hc.hit(1)
hc.hit(2)
hc.hit(3)
print(hc.getHits(4))
hc.hit(300)
print(hc.getHits(300))
print(hc.getHits(301))



