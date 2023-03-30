# Medium graph problem 210: Course Schedule II
# https://leetcode.com/problems/course-schedule-ii/

from collections import deque
from collections import defaultdict


# Time: O(N) Space: O(N)
class Solution:
    def findOrder(self, numCourses, prerequisites):
        """
        :param numCourses: int
        :param prerequisites: List[List[int]]
        :return: List[int]
        """
        graph = defaultdict(list)
        indegrees = {}
        results = []

        # Create graph and record indegrees
        for next_course, first_course in prerequisites:
            graph[first_course].append(next_course)
            indegrees[next_course] = indegrees.get(next_course, 0) + 1

        indegrees_0_q = deque(course for course in range(numCourses) if course not in indegrees)

        while indegrees_0_q:
            node = indegrees_0_q.popleft()
            results.append(node)

            # if node in graph:
            for neighbor in graph[node]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    indegrees_0_q.append(neighbor)

        return results if len(results) == numCourses else []


# Test
s = Solution()
n = 4
prereqs = [[1, 0],
           [2, 0],
           [3, 1],
           [3, 2]]
print(s.findOrder(n, prereqs))
