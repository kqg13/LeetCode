# Running median: https://www.hackerrank.com/challenges/find-the-running-median

# Given an input stream of  integers, perform the following task for each ith int:
#
# 1)    Add the ith int to a running list of integers.
# 2)    Find the median of the updated list (i.e., for the first element through the ith element).
# 3)    Print the updated median on a new line. The printed val must be a double-precision number scaled to 1 decimal


import heapq


def runningMedian(a):
    min_heap, max_heap = [a[0]], []
    heapq.heapify(min_heap)
    heapq.heapify(max_heap)
    results, running_median, n = [float('{0:.1f}'.format(a[0]))], a[0], len(a)
    for i in range(1, n):
        element = a[i]
        if element <= running_median:
            heapq.heappush(max_heap, -element)
        else:
            heapq.heappush(min_heap, element)
        len_min_heap, len_max_heap = len(min_heap), len(max_heap)
        if len_min_heap == len_max_heap:
            running_median = (min_heap[0] - max_heap[0]) / 2
        if len_min_heap - len_max_heap == 1:
            running_median = min_heap[0]
        if len_max_heap - len_min_heap == 1:
            running_median = -max_heap[0]
        if len_min_heap - len_max_heap == 2:
            min_heap_root = heapq.heappop(min_heap)
            heapq.heappush(max_heap, -min_heap_root)
            running_median = (min_heap[0] - max_heap[0]) / 2
        if len_max_heap - len_min_heap == 2:
            max_heap_root = heapq.heappop(max_heap)
            heapq.heappush(min_heap, -max_heap_root)
            running_median = (-max_heap[0] + min_heap[0]) / 2
        results.append(float('{0:.1f}'.format(running_median)))
    return results


a1 = [12, 4, 5, 3, 8, 7]
a2 = [7, 3, 5, 2]
print(runningMedian(a1))
print(runningMedian(a2))

