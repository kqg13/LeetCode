# Graph / Topological Sort Application #310: Minimum Height Trees

# A tree is an undirected graph in which any 2 vertices are connected by exactly one path.
# In other words, any connected graph without simple cycles is a tree.

# Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges where
# edges[i] = [ai, bi] indicates that there is an undirected edge between the two nodes
# ai and bi in the tree, you can choose any node of the tree as the root.

# When you select a node x as the root, the result tree has height h.
# Among all possible rooted trees, those with minimum height (i.e. min(h))
# are called minimum height trees (MHTs).

# Return a list of all MHTs' root labels. You can return the answer in any order.


from collections import deque
from collections import defaultdict

# Approach: starting with leaves furthest away from centroid, continuously trim leaves and work
# our way in until we only have 1 or 2 nodes left in the queue which will be centroids/roots.
# In each step we move closer to the centroids until the trimming process terminates.


# Time: O(V)
class Solution:
    def findMinHeightTrees(self, n, edges):
        """
        :param n: int
        :param edges: List[List[int]]
        :return: List[int]
        """
        if n == 1 or n == 2: return [v for v in range(n)]
        self.graph = defaultdict(list, {v: list() for v in range(n)})
        self.buildGraph(edges)
        leaves_q = deque([v for v in range(n) if len(self.graph[v]) == 1])
        # leaves_q = deque([[v, [v]] for v in range(n) if len(self.graph[v]) == 1])
        rootsList = self.topSort(n, leaves_q)
        return rootsList

    def topSort(self, n, leaves_q):
        while len(leaves_q) >= 2:
            q_size = len(leaves_q)
            n -= q_size
            for _ in range(q_size):
                # pop the leaf defined by "indegree" of 1
                leaf = leaves_q.popleft()
                # remove the leaf edge
                neighbor = self.graph[leaf].pop()
                # remove the corresponding edge
                self.graph[neighbor].remove(leaf)

                if len(self.graph[neighbor]) == 1:
                    leaves_q.append(neighbor)
            if n == 1 or n == 2:
                return list(leaves_q)

    def topSortEli(self, leaves_q):
        while len(leaves_q) > 1:
            node, path = leaves_q.popleft()
            for neighbor in self.graph[node]:
                self.graph[neighbor].remove(node)
                if len(self.graph[neighbor]) == 1:
                    path.copy().append(neighbor)
                    leaves_q.append([neighbor, path])

    def buildGraph(self, edges):
        for v, w in edges:
            self.graph[v].append(w)
            self.graph[w].append(v)


s = Solution()
n1, edges1 = 4, [[1, 0], [1, 2], [1, 3]]  # Expected: [1]
n2, edges2 = 6, [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]  # Expected: [3, 4]
n3, edges3 = 1, []  # Expected: [0]
n4, edges4 = 2, [[0, 1]]  # Expected: [0, 1]
n5, edges5 = 3, [[0, 1], [0, 2]]  # Expected: [0]
n6, edges6 = 6, [[0, 1], [0, 2], [0, 3], [3, 4], [4, 5]]  # Expected: [3]

print(s.findMinHeightTrees(n1, edges1))
# print(s.findMinHeightTrees(n2, edges2))
# print(s.findMinHeightTrees(n3, edges3))
# print(s.findMinHeightTrees(n4, edges4))
# print(s.findMinHeightTrees(n5, edges5))
print(s.findMinHeightTrees(n6, edges6))
