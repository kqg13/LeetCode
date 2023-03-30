# 1884: Egg Drop With 2 Eggs and N Floors
# https://leetcode.com/problems/egg-drop-with-2-eggs-and-n-floors/


class Solution:
    def twoEggDrop(self, n):
        """
        :type n: int
        :rtype: int
        """
        results = [0] * (n + 1)
        p_list = [0] * (n + 1)

        for i in range(1, n + 1):
            for j in range(1, i + 1):
                p_list[j] = max(j, 1 + results[i - j])
            results[i] = min(p_list[1:i + 1])
        return results[n]


s = Solution()
n1, n2, n3 = 2, 3, 4
print(s.twoEggDrop(100))

