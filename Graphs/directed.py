# DFS of a directed graph

from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.results = []

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs_helper(self, v, visited):
        visited[v] = True
        self.results.append(v)
        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                self.dfs_helper(neighbor, visited)

    def dfs(self, v):
        visited = [False] * len(self.graph)
        self.dfs_helper(v, visited)


# Test
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)
# print(g.graph.items())
g.dfs(2)
print(g.results)

