# 901: Online Stock Span
# https://leetcode.com/problems/online-stock-span/description/

from typing import List


class StockSpanner:
    def __init__(self):
        self.prices = []
        self.span = []
        self.stack = []

    def next(self, price: int) -> int:
        self.prices.append(price)
        self.span.append(1)
        n = len(self.prices)
        if n > 1:
            current_px, prev_px = self.prices[-1], self.prices[-2]
            if current_px >= prev_px:
                prev_idx = n - 2
                accumulator = 1
                while current_px >= prev_px:
                    prev_span = self.span[prev_idx]
                    accumulator += prev_span
                    prev_idx -= prev_span
                    if prev_idx < 0:
                        break
                    prev_px = self.prices[prev_idx]
                self.span[-1] = accumulator
        return self.span[-1]

    def next_optimal(self, price: int) -> int:
        ans = 1
        while self.stack and self.stack[-1][0] <= price:
            ans += self.stack.pop()[1]
        self.stack.append([price, ans])
        return ans


ss = StockSpanner()
