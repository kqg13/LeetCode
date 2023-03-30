# Graph Problem #207: Can Finish

# There are a total of numCourses courses you have to take, labeled
# from 0 to numCourses - 1. You are given an array prerequisites where
# prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
#
# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.
#
# Examples:
# numCourses1 = 2, prerequisites1 = [[1, 0]] --> True
# numCourses2 = 2, prerequisites2 = [[1, 0], [0, 1]] --> False

from collections import defaultdict
from collections import deque


class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        self.graph = defaultdict(list, {course: list() for course in range(numCourses)})
        self.indegrees = defaultdict(int)
        self.buildGraph(prerequisites)
        print(self.graph)
        print(self.indegrees)
        zero_indegrees_q = deque(course for course in range(numCourses) if course not in self.indegrees)
        return self.topSort(numCourses, zero_indegrees_q)

    def topSort(self, numCourses, zero_indegrees_q):
        courseCount = 0
        while zero_indegrees_q:
            courseNum = zero_indegrees_q.popleft()
            courseCount += 1

            for nextCourse in self.graph[courseNum]:
                self.indegrees[nextCourse] -= 1
                if self.indegrees[nextCourse] == 0:
                    zero_indegrees_q.append(nextCourse)
                    del self.indegrees[nextCourse]
        return courseCount == numCourses

    def buildGraph(self, prerequisites):
        for secondCourse, firstCourse in prerequisites:
            self.graph[firstCourse].append(secondCourse)
            self.indegrees[secondCourse] += 1


s = Solution()
numCourses1, prereqs1 = 2, [[1, 0]]
numCourses2, prereqs2 = 2, [[1, 0], [0, 1]]
numCourses3, prereqs3 = 3, [[1, 0], [2, 0]]
numCourses4, prereqs4 = 5, [[1, 4], [2, 4], [3, 1], [3, 2]]
numCourses5, prereqs5 = 3, [[1, 0], [0, 1], [0, 2]]
s.canFinish(numCourses5, prereqs5)

