# 526: Beautiful Arrangement
# https://leetcode.com/problems/beautiful-arrangement/description/?envType=problem-list-v2&envId=backtracking


class Solution:
    def countArrangement(self, n: int) -> int:
        self.result = 0
        visited = {i for i in range(1, n + 1)}
        self.counterArrangementHelper(1, visited)
        return self.result

    def counterArrangementHelper(self, index, visited):
        # Base cases
        if not visited:
            self.result += 1
            return

        visited_copy = visited.copy()

        for i in visited_copy:
            if i % index == 0 or index % i == 0:
                visited.remove(i)
                self.counterArrangementHelper(index + 1, visited)
                visited.add(i)


s = Solution()
n1 = 2  # Expected: 2
n2 = 1  # Expected: 1
n3 = 3  # Expected: 3
