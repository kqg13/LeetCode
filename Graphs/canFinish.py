# Graph Problem 207: Can Finish

from collections import defaultdict

class Solution:
    def canFinish(self, numCourses, prerequisites):
        indegrees = [0] * numCourses
        graph = self.getIndegrees(indegrees, prerequisites)
        visited = [False] * numCourses
        zero_indegrees = [i for i, x in enumerate(indegrees) if x == 0]
        if zero_indegrees:
            for node in zero_indegrees:
                canSchedule = self.dfs(visited, node, graph)
            if not all(visited):
                return False
            else:
                return canSchedule
        else:
            return False

    def dfs(self, visited, node, graph):
        if visited[node]:
            return False
        visited[node] = True
        for neighbor in graph[node]:
            canSchedule = self.dfs(visited, neighbor, graph)
            if not canSchedule:
                return False
        return True

    def getIndegrees(self, indegrees, prerequisities):
        graph = defaultdict(list)
        for first_course, second_course in prerequisities:
            graph[first_course].append(second_course)
            indegrees[second_course] += 1
        return graph


s = Solution()
n = 3
prereqs = [[1, 0], [2, 0]]
print(s.canFinish(n, prereqs))
