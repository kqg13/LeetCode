from collections import Counter
from collections import defaultdict


def solution(A):
    counter = Counter(A)
    for v in counter.values():
        if v % 2 == 1:
            return False
    return True


def solution2(N):
    wrong_list = [1] * N
    return wrong_list


def solution3(S):
    count = 1
    the_dict = dict()
    n = len(S)
    for i in range(n):
        if S[i] in the_dict:
            count += 1
            the_dict.clear()
        the_dict[S[i]] = None
    return count


# Given an int N, return the smallest non-negative number whose individual digits sum up to N.
# https://leetcode.com/discuss/interview-question/1726332/Microsoft-Online-Assessment-Questions
def smallest_number(N):
    no_nines = N // 9
    res = N % 9
    while no_nines > 0:
        res = res * 10 + 9
        no_nines -= 1
    return res


# https://leetcode.com/discuss/interview-question/1724938/Microsoft-online-OA
class Solution:
    def BiggestTerritory(self, m):
        self.matrix = m
        self.directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        self.PadMatrix()
        current, result = 1, 1
        m, n = len(self.matrix), len(self.matrix[0])
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                territory = self.matrix[i][j]
                if territory != 'X':
                    current = self.dfs(territory, 0, i, j)
                result = max(result, current)
        return result

    def dfs(self, territory, count, r, c):
        self.matrix[r][c] = 'X'
        count += 1
        for dr, dc in self.directions:
            new_r, new_c = r + dr, c + dc
            if self.matrix[new_r][new_c] == territory:
                count = self.dfs(territory, count, new_r, new_c)
        return count

    def PadMatrix(self):
        self.PadCols()
        self.PadRows()

    def PadCols(self):
        for row in self.matrix:
            row.insert(0, 'X')
            row.append('X')

    def PadRows(self):
        n = len(self.matrix[0])
        row = ['X'] * n
        self.matrix.insert(0, row)
        self.matrix.append(row)


# Longest Alternating Path
# https://leetcode.com/discuss/interview-question/1581861/microsoft-oa-longest-alternating-path
class UndirectedGraph(object):
    def __init__(self, S, parents):
        self.S = S
        self.parents = parents
        self.N = len(self.S)
        self.graph = defaultdict(list, {v: [] for v in range(self.N)})
        self.result = 1

    def GetEdges(self):
        edges = list()
        for i in range(self.N):
            if self.parents[i] != -1:
                temp = [i, self.parents[i]]
                edges.append(temp)
        return edges

    def BuildGraph(self):
        edges = self.GetEdges()
        for v, w in edges:
            self.graph[v].append(w)
            self.graph[w].append(v)

    def LongestPath(self):
        self.BuildGraph()


    def dfs(self, current):
        pass


# solution
a1 = [1, 2, 2, 1]
a2 = [7, 7, 7]
a3 = [1, 2, 2, 3]
# print(solution(a3))
# solution2
n1 = 6
# print(solution2(n1))
# solution3
s1 = "world"
s2 = "dddd"
s3 = "cycle"
s4 = "abacdec"
# print(smallest_number(21))

matrix1 = [[4, 4, 6, 2, 8, 0],
           [1, 4, 6, 3, 2, 9],
           [2, 9, 8, 9, 9, 9],
           [9, 9, 3, 7, 9, 9],
           [3, 3, 3, 6, 7, 0],
           [3, 3, 5, 6, 5, 0]]
s = Solution()
print(s.BiggestTerritory(matrix1))
S1, A1 = "abbab", [-1, 0, 0, 0, 2]
ug = UndirectedGraph(S1, A1)
ug.BuildGraph()
