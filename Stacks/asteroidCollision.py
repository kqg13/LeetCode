# 735: Asteroid Collision
# https://leetcode.com/problems/asteroid-collision/description/

from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        index, n = 1, len(asteroids)
        stack = [asteroids[0]]
        while index < n:
            asteroid = asteroids[index]
            if asteroid > 0 or not stack:
                stack.append(asteroid)
                index += 1
            else:
                t = stack[-1]
                if t < 0:
                    stack.append(asteroid)
                    index += 1
                else:
                    del stack[-1]
                    abs_asteroid = abs(asteroid)
                    if t == abs_asteroid:
                        index += 1
                    elif t > abs_asteroid:
                        stack.append(t)
                        index += 1
        return stack


s = Solution()
asteroids1 = [5, 10, -5]  # Expected: [5, 10]
asteroids2 = [8, -8]  # Expected: []
asteroids3 = [10, 2, -5]  # Expected: [10]
asteroids4 = [3, 5, -6, 2, -1, 4]  # Expected: [-6, 2, 4]
