# Implementation of undirected graph with cycle detection

# Note: assume no duplicate edges will appear in edges input and no self loops.
# Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.


from collections import defaultdict


class UndirectedGraph(object):
    def __init__(self, nVertices, edges):
        self.n = nVertices
        self.edges = edges
        self.graph = defaultdict(list, {v: [] for v in range(self.n)})
        self.visited = [False] * self.n
        self.buildGraph()

    def buildGraph(self):
        for v, w in self.edges:
            self.graph[v].append(w)
            self.graph[w].append(v)

    def addEdge(self, v, w):
        if v == w:
            raise Exception("No self loops permitted")
        elif (v in self.graph and w in self.graph[v]) or (w in self.graph and v in self.graph[w]):
            edge = "[" + str(v) + ", " + str(w) + "]"
            raise Exception("Cannot add " + edge + " because it already exists")
        else:
            self.graph[v].append(w)
            self.graph[w].append(v)

    def detectCycleHelper(self, node, parent):
        self.visited[node] = True
        for neighbor in self.graph[node]:
            if not self.visited[neighbor]:
                hasCycle = self.detectCycleHelper(neighbor, node)
                if hasCycle:
                    return True
            # if node is in visited and not simply a 'cycle' due to definition of undirected edge
            elif neighbor != parent:
                return True
        return False

    def detectCycle(self):
        for v in range(self.n):
            if not self.visited[v]:
                if self.detectCycleHelper(v, -1):
                    return True
        return False


n1, edges1 = 5, [[0, 1], [1, 2], [2, 3], [3, 4]]
n2, edges2 = 5, [[0, 1], [1, 2]]
n3, edges3 = 5, []
n4, edges4 = 5, [[0, 1], [0, 2], [0, 3], [1, 0], [1, 2], [2, 0], [2, 1], [3, 0], [3, 4], [4, 3]]
ug = UndirectedGraph(n4, edges4)
# ug.addEdge(1, 0)
# ug.addEdge(1, 2)
# ug.addEdge(2, 0)
# ug.addEdge(0, 3)
# ug.addEdge(3, 4)
print(ug.detectCycle())
