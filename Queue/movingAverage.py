# Easy queue problem 346: Moving Average from Data Stream

# Given a stream of integers and a window size, calculate the moving average
# of all integers in the sliding window.

# Example:
# MovingAverage m = new MovingAverage(3);
# m.next(1) = 1
# m.next(10) = (1 + 10) / 2
# m.next(3) = (1 + 10 + 3) / 3
# m.next(5) = (10 + 3 + 5) / 3

from collections import deque


class MovingAverage:

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.size = size
        self.d = deque(maxlen=self.size)

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.d.append(val)
        return sum(self.d) / len(self.d)
