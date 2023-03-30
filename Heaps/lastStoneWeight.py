# 1046: Last Stone Weight
# https://leetcode.com/problems/last-stone-weight/


import heapq


# Time: O(NlogN)
class Solution:
    def lastStoneWeight(self, stones) -> int:
        max_heap = [-1 * stone for stone in stones]
        heapq.heapify(max_heap)
        while len(max_heap) >= 2:
            largest = heapq.heappop(max_heap)
            second_largest = heapq.heappop(max_heap)
            if largest != second_largest:
                new_stone = largest - second_largest
                heapq.heappush(max_heap, new_stone)
        return 0 if len(max_heap) == 0 else -max_heap[0]


s = Solution()
stones1 = [2, 7, 4, 1, 8, 1]
stones2 = [2, 2]
print(s.lastStoneWeight(stones1))
print(s.lastStoneWeight(stones2))
