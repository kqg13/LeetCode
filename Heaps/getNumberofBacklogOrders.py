# 1801: Number of Orders in the Backlog
# https://leetcode.com/problems/number-of-orders-in-the-backlog/description/

from typing import List
import heapq


class Solution:
    # O(NlogN): Time; O(N): Space
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        result_mod = 10**9 + 7
        buy_heap, sell_heap = [], []

        for px, amt, order_type in orders:
            if order_type == 0:
                while len(sell_heap) > 0 and amt > 0:
                    sell_px, sell_amt = sell_heap[0]
                    if sell_px > px: break
                    apply_amt = min(sell_amt, amt)
                    amt -= apply_amt
                    if apply_amt == sell_amt:
                        heapq.heappop(sell_heap)
                    else:
                        sell_heap[0][1] -= apply_amt
                if amt > 0:
                    heapq.heappush(buy_heap, [-px, amt])
            else:
                while len(buy_heap) > 0 and amt > 0:
                    buy_px, buy_amt = -buy_heap[0][0], buy_heap[0][1]
                    if buy_px < px: break
                    apply_amt = min(buy_amt, amt)
                    amt -= apply_amt
                    if apply_amt == buy_amt:
                        heapq.heappop(buy_heap)
                    else:
                        buy_heap[0][1] -= apply_amt
                if amt > 0:
                    heapq.heappush(sell_heap, [px, amt])

        total_backlog = sum(item[1] for item in buy_heap) + sum(item[1] for item in sell_heap)
        return total_backlog % result_mod


s = Solution()
orders1 = [[10, 5, 0], [15, 2, 1], [25, 1, 1], [30, 4, 0]]  # Expected: 6
orders2 = [[7, 1000000000, 1], [15, 3, 0], [5, 999999995, 0], [5, 1, 1]]  # Expected: 999999984
