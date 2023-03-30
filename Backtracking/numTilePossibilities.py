# LeetCode Problem 1079: Letter Tile Possibilities

# You have n tiles, where each tile has one letter tiles[i] printed on it.
# Return the # of possible non-empty sequences of letters you can make using
# the letters printed on those tiles.

# Examples:
# Input: tiles1 = "AAB" ---> 8
# Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA"
# Input: tiles2 = "AAABBC" ---> 188
# Input: tiles3 = "V" ---> 1


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        self.results = set()
        self.n = len(tiles)
        self.visited = [False] * self.n
        self.tileHelper(tiles, '')
        return len(self.results) - 1

    def tileHelper(self, tiles: str, current):
        self.results.add(current)
        for i in range(self.n):
            if not self.visited[i]:
                self.visited[i] = True
                self.tileHelper(tiles, current + tiles[i])
                self.visited[i] = False


s = Solution()
tiles1, tiles2, tiles3 = "AAB", "AAABBC", "V"
print(s.numTilePossibilities(tiles1))
