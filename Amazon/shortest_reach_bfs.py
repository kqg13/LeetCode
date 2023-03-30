# HackerRank: Shortest Reach in a Graph
# https://www.hackerrank.com/challenges/ctci-bfs-shortest-reach/problem

# Consider an undirected graph consisting of  nodes where each node is labeled from 1 to N
# and the edge between any two nodes is always of length . We define node S to be starting position for a BFS.
# Given a graph, determine the distances from the start node to each of its descendants and return
# the list in node number order, ascending. If a node is disconnected, it's distance should be -1.

from collections import defaultdict
from collections import deque


class Graph(object):
    def __init__(self, n, edges):  # edges for testing only
        self.n = n
        self.edges = edges  # to remove: for testing only
        self.graph = defaultdict(list, {v: [] for v in range(self.n)})
        self.visited = [False] * self.n
        self.distances = [-1] * (self.n)

    def connect(self, u, v):
        # to remove: testing
        for a, b in self.edges:
            self.graph[a - 1].append(b - 1)
            self.graph[b - 1].append(a - 1)
        # self.graph[u].append(v)
        # self.graph[v].append(u)

    def find_all_distances(self, s):
        self.connect(0, 0)
        q = deque([s])
        self.distances[s] = 0
        while q:
            node = q.popleft()
            self.visited[node] = True
            for neighbor in self.graph[node]:
                if self.visited[neighbor] or neighbor in q:
                    continue
                self.distances[neighbor] = self.distances[node] + 6
                q.append(neighbor)
        del self.distances[s]
        output = ' '.join(map(str, self.distances))
        return output


edges1 = [[1, 2], [2, 3], [3, 4], [1, 5], [1, 3]]
graph1 = Graph(6, edges1)
print(graph1.find_all_distances(0))
