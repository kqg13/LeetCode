# 935: Knight Dialer
# https://leetcode.com/problems/knight-dialer/description/

from functools import cache


class Solution:
    def knightDialer(self, n: int) -> int:
        self.moves = \
            {
                1: [6, 8],
                2: [7, 9],
                3: [4, 8],
                4: [0, 3, 9],
                5: [],
                -1: [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
                6: [0, 1, 7],
                7: [2, 6],
                8: [1, 3],
                9: [2, 4],
                0: [4, 6]
            }
        self.results = list()
        self.count = 0
        self.knightDialerHelper(n, -1, "")
        print(self.results, self.count)
        return self.count

    def knightDialerHelper(self, n, num, current):  # num is where you came from
        # Base
        if n == 1:
            for dial in self.moves[num]:
                extended_dial = current + str(dial)
                self.results.append(extended_dial)
                self.count += 1
            return
        for dial in self.moves[num]:
            extended_dial = current + str(dial)
            self.knightDialerHelper(n - 1, dial, extended_dial)

    # Top-down / Cache
    def knightDialerCache(self, n) -> int:
        self.bound = (10 ** 9) + 7
        self.movesOriginal = \
            {
                1: [6, 8],
                2: [7, 9],
                3: [4, 8],
                4: [0, 3, 9],
                5: [],
                6: [0, 1, 7],
                7: [2, 6],
                8: [1, 3],
                9: [2, 4],
                0: [4, 6]
            }

        result = 0
        for square in self.movesOriginal:
            # on starting square we make n - 1 jumps because starting square has already contributed 1
            result = (result + self.knightDialerCacheHelper(n - 1, square)) % self.bound
        return result

    @cache
    def knightDialerCacheHelper(self, remain, square) -> int:
        # we are on the last square which contributes 1
        if remain == 0:
            return 1
        result = 0
        for dial in self.movesOriginal[square]:
            result = (result + self.knightDialerCacheHelper(remain - 1, dial)) % self.bound
        return result


s = Solution()
n1, n2, n3, n4 = 1, 2, 3, 3131
