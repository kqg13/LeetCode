# 2126: Destroying Asteroids
# https://leetcode.com/problems/destroying-asteroids/description/

from typing import List


class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids_sorted = sorted(asteroids)
        for asteroid in asteroids_sorted:
            if mass >= asteroid:
                mass += asteroid
            else:
                return False
        return True


s = Solution()
mass1, asteroids1 = 10, [3, 9, 19, 5, 21]  # Expected: True
mass2, asteroids2 = 5, [4, 9, 23, 4]   # Expected: False
