# River sizes: Graph Problem

# You are given a 2-D matrix of potentially unequal height and width containing
# only 0s and 1s. Each 0 represents land, and each 1 represents part of a
# river. A river consists of any number of 1s that are either horizontally or
# vertically adjacent (but not diagonally adjacent). The number of adjacent 1s
# forming a river determine its size. Write a function that returns an array of
# the sizes of all rivers represented in the input matrix. Note that these
# sizes do not need to be in any particular order.

# Sample input:
# [[1, 0, 0, 1, 0],
#  [1, 0, 1, 0, 0],
#  [0, 0, 1, 0, 1],
#  [1, 0, 1, 0, 1],
#  [1, 0, 1, 1, 0]]
# Sample output: [1, 2, 2, 2, 5]


def river_sizes(matrix):
    pad_matrix(matrix)
    visited = create_visited(matrix)
    m, n = len(matrix), len(matrix[0])
    rivers = []
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] and not visited[i][j]:
                riversize = dfs(matrix, visited, i, j)
                rivers.append(riversize)
    print(rivers)
    return rivers


def dfs(matrix, visited, i, j, rsize=0):
    neighbors = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
    visited[i][j] = True
    rsize += 1
    for n1, n2 in neighbors:
        if matrix[n1][n2] and not visited[n1][n2]:
            rsize = dfs(matrix, visited, n1, n2, rsize)
    return rsize


def pad_matrix(matrix):
    n = len(matrix[0])  # original cols
    # Pad cols
    for row in matrix:
        row.insert(0, 0)
        row.append(0)
    # Pad rows
    t = [0] * (n + 2)
    matrix.append(t)
    matrix.insert(0, t)


def create_visited(matrix):
    visited = []
    m, n = len(matrix), len(matrix[0])
    for i in range(m):
        row = []
        for j in range(n):
            row.append(False) if matrix[i][j] == 1 else row.append(True)
        visited.append(row)
    return visited


mx = [
        [1, 0, 0, 1, 0],
        [1, 0, 1, 0, 0],
        [0, 0, 1, 0, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 1, 1, 0]
    ]
river_sizes(mx)
