# 77: Combinations


class Solution:
    def combine(self, n: int, k: int):
        self.results = list()
        self.n = n
        self.k = k
        self.combineHelper([], 1, 0)
        return self.results

    def combineHelper(self, current, start_num, depth):
        # Base
        print(current)
        if len(current) == self.k:
            self.results.append(current.copy())
            return

        end = self.n - (self.k - depth - 1)
        for i in range(start_num, end + 1):
            current.append(i)
            self.combineHelper(current, i + 1, depth + 1)
            current.pop()


n1, k1 = 4, 2  # [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
s = Solution()
s.combine(n1, k1)
