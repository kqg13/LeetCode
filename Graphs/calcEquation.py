# 399: Evaluate Division
# https://leetcode.com/problems/evaluate-division/

from collections import defaultdict


class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        self.results = list()
        self.graph = defaultdict(list)
        self.buildGraph(equations, values)
        print(self.graph)
        # dfs on each query
        for query in queries:
            self.evaluateQuery(query)

        return self.results

    def buildGraph(self, equations, values):
        for (e0, e1), v in zip(equations, values):
            self.graph[e0].append((e1, v))
            self.graph[e1].append((e0, 1 / v))

    def evaluateQuery(self, query):
        source, target = query
        if source not in self.graph or target not in self.graph:
            self.results.append(-1)
            return
        if source == target:
            self.results.append(1)
            return

        visited = set()
        result = 1
        self.dfs(source, target, visited, result)
        if target not in visited:
            self.results.append(-1)

    def dfs(self, source, target, visited, result):
        if target in visited:
            return
        visited.add(source)

        for neighbor, edge in self.graph[source]:
            if neighbor in visited:
                continue
            if neighbor == target:
                visited.add(neighbor)
                self.results.append(result * edge)
                break
            updated_result = result * edge
            self.dfs(neighbor, target, visited, updated_result)


s = Solution()
equations1 = [["a", "b"], ["b", "c"]]
values1 = [2.0, 3.0]
queries1 = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
s.calcEquation(equations1, values1, queries1)

equations2 = [["a", "b"], ["b", "c"], ["bc", "cd"]]
values2 = [1.5, 2.5, 5.0]
queries2 = [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]]
s.calcEquation(equations2, values2, queries2)

equations3 = [["a", "b"]]
values3 = [0.5]
queries3 = [["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]]
s.calcEquation(equations3, values3, queries3)
