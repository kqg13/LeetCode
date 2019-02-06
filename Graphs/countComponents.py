# Medium graph problem 323: # of Connected Components in an Undirected Graph

# Given n nodes labeled from 0 to n - 1 and a list of undirected
# edges (each edge is a pair of nodes), write a function to find the number
# of connected components in an undirected graph.

# Example 1:
# Input: n = 5 and edges = [[0, 1], [1, 2], [3, 4]]
#    0          3
#    |          |
#    1 --- 2    4
# Output: 2

# Example 2:
# Input: n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
#     0           4
#     |           |
#     1 --- 2 --- 3
# Output: 1


class Solution:
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        self.count = 0
        self. graph = {i: list() for i in range(n)}
        self.visited = []

        for i, j in edges:
            self.graph[i].append(j)
            self.graph[j].append(i)

        def dfs_helper(node):
            self.visited.append(node)
            for neighbor in self.graph[node]:
                if neighbor not in self.visited:
                    dfs_helper(neighbor)

        for node in range(0, n):
            if node not in self.visited:
                self.count += 1
                dfs_helper(node)

        return self.count
