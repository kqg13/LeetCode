# Graph problem #261: Graph Valid Tree

# Given n nodes labeled from 0 to n-1 and a list of undirected edges
# (each edge is a pair of nodes), write a function to check whether these
# edges make up a valid tree.

# Examples:
# Input: n1 = 5, edges1 = [[0, 1], [0, 2], [0, 3], [1, 4]] --> True
# Input: n2 = 5, edges2 = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]] --> False


# Time: O(V + E), Space: O(V + E)
class Solution:
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        self.n, self.edges = n, edges
        self.visited = [False] * self.n
        self.graph = {v: list() for v in range(n)}
        self.buildGraph()

        noCycle = self.validTreeHelper(0, -1)
        # connected?
        if noCycle:
            return all(self.visited)
        return False

    def validTreeHelper(self, node, parent):
        self.visited[node] = True
        for neighbor in self.graph[node]:
            if neighbor == parent:
                continue
            if self.visited[neighbor] and neighbor != parent:
                return False
            if not self.validTreeHelper(neighbor, node):
                return False
        return True

    def buildGraph(self):
        for v, w in self.edges:
            self.graph[v].append(w)
            self.graph[w].append(v)


s = Solution()
n1, edges1 = 5, [[0, 1], [0, 2], [0, 3], [1, 4]]
n2, edges2 = 5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
# print(s.validTree(n1, edges1))
print(s.validTree(n2, edges2))
