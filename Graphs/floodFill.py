# Graph problem 733: Flood Fill

# An image is represented by a 2-D array of integers, each int representing
# the pixel value of the image (from 0 to 65535). Given a coordinate (sr, sc)
# representing the starting pixel (row and column) of the flood fill, and a
# pixel value newColor, "flood fill" the image.

# To perform a "flood fill", consider the starting pixel, plus any pixels
# connected 4-directionally to the starting pixel of the same color as the
# starting pixel, plus any pixels connected 4-directionally to those pixels
# (also with the same color as the starting pixel), and so on.
# Replace the color of all of the aforementioned pixels with the newColor.

# At the end, return the modified image.

# Example input:
# image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]], sr = 1, sc = 1, newColor = 2
# output = [[2, 2, 2], [2, 2, 0],[2, 0, 1]]


# Time: O(MN) Space: O(MN) implicit size of call stack
class Solution:
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    def floodFill(self, image, sr, sc, newColor):
        startColor, m, n = image[sr][sc], len(image), len(image[0])
        image[sr][sc] = newColor
        startNode = (sr, sc)
        self.dfs(image, startColor, newColor, m, n, startNode, set())
        return image

    def dfs(self, image, startColor, newColor, m, n, node, visited):
        r, c = node
        if node in visited or r < 0 or r >= m or c < 0 or c >= n:
            return
        visited.add(node)
        for direction in self.directions:
            neighbor = (node[0] + direction[0], node[1] + direction[1])
            neighborR, neighborC = neighbor
            if (m > neighborR >= 0) and (n > neighborC >= 0):
                if image[neighborR][neighborC] == startColor:
                    image[neighborR][neighborC] = newColor
                    self.dfs(image, startColor, newColor, m, n, neighbor, visited)

    # Not used
    def padMatrix(self, image):
        n = self.padCols(image)
        newRow = ['X'] * n
        self.padRows(image, newRow)

    def padCols(self, image):
        for row in image:
            row.insert(0, 'X')
            row.append('X')
        return len(image[0])

    def padRows(self, image, newRow):
        image.insert(0, newRow)
        image.append(newRow)


s = Solution()
img = [
        [1, 1, 1],
        [1, 1, 0],
        [1, 0, 1]
      ]
sr, sc, nc = 1, 1, 2
