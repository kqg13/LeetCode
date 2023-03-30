# Problem 797: All Paths From Source to Target

# Given a (DAG) of n nodes labeled from 0 to n - 1, find all possible paths
# from node 0 to node n - 1, and return them in any order.
#
# The graph is given as follows: graph[i] is a list of all nodes you can visit
# from node i (i.e., there is a directed edge from node i to node graph[i][j]).

# Examples:
# Input: graph1 = [[1, 2], [3], [3], []]
# Output: [[0, 1, 3], [0, 2, 3]]
# Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3

# Input: graph2 = [[4, 3, 1], [3, 2, 4], [3], [4], []]
# Output: [[0, 4], [0, 3, 4], [0, 1, 3, 4], [0, 1, 2, 3, 4], [0, 1, 4]]

# Input: graph3 = [[1, 2, 3], [2], [3], []]
# Output: [[0, 1, 2, 3], [0, 2, 3], [0, 3]]

# Input: graph4 = [[1, 3], [2], [3], []]
# Output: [0, 1, 2, 3], [0, 3]]

# Time: O(2^N * N) # Space: O(2^N * N); stack space: O(N)
class Solution:
    # noinspection PyPep8Naming
    def allPathsSourceTarget(self, graph: list) -> list:
        self.results, currentPath = [], []
        self.n = len(graph) - 1
        currentPath.append(0)
        self.dfs(graph, currentPath, 0)
        print(self.results)
        return self.results

    # noinspection PyPep8Naming
    def dfs(self, graph, currentPath, node):
        if node == self.n:
            self.results.append(currentPath.copy())
            return
        edges = graph[node]
        for edge in edges:
            currentPath.append(edge)
            self.dfs(graph, currentPath, edge)
            currentPath.pop()


s = Solution()
graph1 = [[1, 2], [3], [3], []]
graph2 = [[4, 3, 1], [3, 2, 4], [3], [4], []]
graph3 = [[1, 2, 3], [2], [3], []]
graph4 = [[1, 3], [2], [3], []]

s.allPathsSourceTarget(graph1)
s.allPathsSourceTarget(graph2)
s.allPathsSourceTarget(graph3)
s.allPathsSourceTarget(graph4)
