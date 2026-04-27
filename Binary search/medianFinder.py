# 295: Find Median from Data Stream
# https://leetcode.com/problems/find-median-from-data-stream/description/

class MedianFinder:
    def __init__(self):
        # invariant: remains sorted
        self.container = list()

    def addNum(self, num: int) -> None:
        if not self.container:
            self.container.append(num)
        else:
            idx = self.binary_search(0, len(self.container) - 1, num)
            self.container.insert(idx, num)

    def binary_search(self, low, high, num):
        if high > low:
            mid = (low + high) // 2
            if self.container[mid] == num:
                return mid + 1
            elif self.container[mid] > num:
                return self.binary_search(low, mid - 1, num)
            else:
                return self.binary_search(mid + 1, high, num)
        elif high == low:
            if self.container[low] >= num:
                return low
            else:
                return low + 1
        else:
            return low

    def findMedian(self) -> float:
        n = len(self.container)
        # list is odd in length
        if n % 2 == 1:
            median_idx = int((n - 1) / 2)
            return self.container[median_idx]
        # list is even in length
        else:
            mid_idx = int(n / 2)
            other_mid_idx = mid_idx - 1
            median = (self.container[mid_idx] + self.container[other_mid_idx]) / 2
            return median


# Your MedianFinder object will be instantiated and called as such:
mf = MedianFinder()
mf.addNum(-1)
print(mf.findMedian())
mf.addNum(-2)
print(mf.findMedian())
mf.addNum(-3)
print(mf.findMedian())

