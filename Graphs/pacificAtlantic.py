# Graph problem 417: Pacific Atlantic Water Flow

# Given an m x n matrix of non-negative integers representing the height of
# each unit cell in a continent, the "Pacific ocean" touches the left and top
# edges of the matrix and the "Atlantic ocean" touches the right and bottom edges.
#
# Water can only flow in four directions (up, down, left, or right) from a cell
# to another one with height equal or lower. Find the list of grid coordinates
# where water can flow to both the Pacific and Atlantic ocean.

# Given the following 5x5 matrix:
#
#   Pacific ~   ~   ~   ~   ~
#        ~  1   2   2   3  (5) *
#        ~  3   2   3  (4) (4) *
#        ~  2   4  (5)  3   1  *
#        ~ (6) (7)  1   4   5  *
#        ~ (5)  1   1   2   4  *
#           *   *   *   *   * Atlantic


class Solution:
    def pacificAtlantic(self, matrix):
        if not matrix: return []
        visited_a, visited_p = set(), set()
        m, n = len(matrix), len(matrix[0])
        self.pad_matrix(matrix)
        self.dfs_pacific(matrix, visited_p, m, n)
        self.dfs_atlantic(matrix, visited_a, m, n)
        result = list(visited_a.intersection(visited_p))
        final = [[a - 1, b - 1] for a, b in result]
        return final

    def dfs_pacific(self, matrix, visited_p, m, n):
        for c in range(1, n + 1):
            node = (1, c)
            self.dfs(matrix, visited_p, node)
        for r in range(2, m + 1):
            node = (r, 1)
            self.dfs(matrix, visited_p, node)

    def dfs_atlantic(self, matrix, visited_a, m, n):
        for c in range(1, n + 1):
            node = (m, c)
            self.dfs(matrix, visited_a, node)
        for r in range(1, m):
            node = (r, n)
            self.dfs(matrix, visited_a, node)

    def dfs(self, matrix, visited, node):
        if node in visited:
            return
        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        visited.add(node)
        for direction in directions:
            neighbor = (node[0] + direction[0], node[1] + direction[1])
            if matrix[neighbor[0]][neighbor[1]] >= matrix[node[0]][node[1]]:
                self.dfs(matrix, visited, neighbor)

    def pad_matrix(self, matrix):
        n = len(matrix[0])  # original cols
        # Pad cols
        for row in matrix:
            row.insert(0, -1)
            row.append(-1)
        # Pad rows
        t = [-1] * (n + 2)
        matrix.append(t)
        matrix.insert(0, t)


matrix = [[1, 2, 2, 3, 5],
          [3, 2, 3, 4, 5],
          [2, 4, 5, 3, 1],
          [6, 7, 1, 4, 5],
          [5, 1, 1, 2, 4]]

matrix2 = [[1, 2],
           [4, 3]]
s = Solution()
print(s.pacificAtlantic(matrix))
# print(s.pacificAtlantic(matrix2))
