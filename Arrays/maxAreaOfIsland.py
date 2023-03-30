# Medium Array/DFS problem 695: Max Area of Island

# Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's
# (representing land) connected 4-directionally (horizontal or vertical.) You
# may assume all four edges of the grid are surrounded by water. Find the max
# area of an island in the given 2D array. If there is no island, max
# area is 0.


class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :param grid: List[List[int]]
        :return: int
        """
        self.n_rows = len(grid)
        self.n_cols = len(grid[0])
        self.max_area = 0

        def count_island(r, c, grid):
            grid[r][c] = -1
            count = 1
            if r > 0 and grid[r - 1][c] == 1:
                count += count_island(r - 1, c, grid)
            if r < self.n_rows - 1 and grid[r + 1][c] == 1:
                count += count_island(r + 1, c, grid)
            if c > 0 and grid[r][c - 1] == 1:
                count += count_island(r, c - 1, grid)
            if c < self.n_cols - 1 and grid[r][c + 1] == 1:
                count += count_island(r, c + 1, grid)

            self.max_area = max(self.max_area, count)
            return count

        for row in range(0, self.n_rows):
            for col in range(0, self.n_cols):
                if grid[row][col] == 1:
                    count_island(row, col, grid)
        return self.max_area


s = Solution()
m = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
[0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
[0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]

print(s.maxAreaOfIsland(m))
