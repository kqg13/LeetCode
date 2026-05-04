# 1010: Pair of Songs with Total Durations Divisible by 60
# https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/description/?envType=company&envId=citadel&favoriteSlug=citadel-more-than-six-months

from typing import List
from collections import defaultdict


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        d = defaultdict(lambda: 0)
        result = 0
        for t in time:
            r = t % 60
            complement = 0 if r == 0 else 60 - r
            if complement in d:
                result += d[complement]
            d[r] += 1
        return result


s = Solution()
time1 = [30, 20, 150, 100, 40]  # Expected: 3
time2 = [60, 60, 60]  # Expected: 3
