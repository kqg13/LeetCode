# 1823: Find the Winner of the Circular Game
# https://leetcode.com/problems/find-the-winner-of-the-circular-game/


class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        circle = [i for i in range(0, n)]
        lastIndex = 0
        while len(circle) > 1:
            print(circle)
            lastIndex = (lastIndex + k) % len(circle)
            print('lastIndex1', lastIndex)
            del circle[lastIndex]
            lastIndex = lastIndex % len(circle)
            print('lastIndex2', lastIndex)
        return circle[0]

    def josephus(self, n, k):
        if n == 1:
            return 0
        return (self.josephus(n - 1, k) + k) % n


s = Solution()
n1, k1 = 5, 2
# print(s.findTheWinner(n1, k1))
print(s.josephus(n1, k1) + 1)
