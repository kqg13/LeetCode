# Implementation of directed graph with: BFS, cycle detection

# Note: assume no duplicate edges will appear in edges input and no self loops.


from collections import defaultdict
from collections import deque


class DirectedGraph(object):
    def __init__(self, nVertices, edges):
        self.n = nVertices
        self.edges = edges
        self.graph = defaultdict(list, {v: [] for v in range(self.n)})
        self.visited = [False] * self.n
        self.buildGraph()

    def buildGraph(self):
        for v, w in self.edges:
            self.graph[v].append(w)
            # self.graph[w].append(v) # you would need this for undirected graph

    def addEdge(self, v, w):
        if v == w:
            raise Exception("No self loops permitted")
        elif v in self.graph and w in self.graph[v]:
            edge = "[" + str(v) + ", " + str(w) + "]"
            raise Exception("Cannot add " + edge + " because it already exists")
        else:
            self.graph[v].append(w)

    def bfs(self, root):
        queue, bfs_results = deque([root]), list()
        # self.visited[root] = True
        while queue:
            node = queue.popleft()
            self.visited[node] = True
            bfs_results.append(node)

            for neighbor in self.graph[node]:
                if not self.visited[neighbor]:
                    queue.append(neighbor)
        return bfs_results

    def bfs2(self, root):
        queue, bfs_results = deque([root]), list()
        self.visited[root] = True
        while queue:
            node = queue.popleft()
            bfs_results.append(node)

            for neighbor in self.graph[node]:
                if not self.visited[neighbor]:
                    queue.append(neighbor)
                    self.visited[neighbor] = True
        return bfs_results


n1, edges1 = 4, [[0, 1], [0, 2], [1, 2], [2, 0], [2, 3], [3, 3]]
dg1 = DirectedGraph(4, edges1)
print(dg1.graph)
print(dg1.bfs(2))

# dg2 = DirectedGraph(4, [])
# dg2.addEdge(0, 1)
# dg2.addEdge(0, 2)
# dg2.addEdge(1, 2)
# dg2.addEdge(2, 0)
# dg2.addEdge(2, 3)
# dg2.addEdge(3, 3)


