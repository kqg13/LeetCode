# LeetCode Problem 79: Word Search

# Given a 2D board and a word, find if the word exists in the grid.
# The word can be constructed from letters of sequentially adjacent cell,
# where "adjacent" cells are those horizontally or vertically neighboring.
# The same letter cell may not be used more than once.

# Given board below and word = "ABCCED", return True.
# Given board below and word = "SEE", return True.
# Given board below and word = "ABCB", return False.


# Running time: O(n * 3^n)
class Solution:
    # right, left, up, down
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited = []

    def exist(self, board, word) -> bool:
        if not word: return True
        self.createVisited(board)
        self.padMatrix(board)
        self.wordLength = len(word) - 1
        for r, row in enumerate(board):
            for c, letter in enumerate(row):
                if letter == word[0]:
                    result = self.dfs(board, r, c, word, 0)
                    if result:
                        return True
        return False

    def dfs(self, board, prevRow, prevCol, word, wordIndex):
        self.visited[prevRow][prevCol] = True
        currentLetter = board[prevRow][prevCol]
        if wordIndex == self.wordLength and currentLetter == word[wordIndex]:
            return True
        elif currentLetter == '' or currentLetter != word[wordIndex]:
            self.visited[prevRow][prevCol] = False
            return False
        else:
            for dr, dc in self.directions:
                rowIndex, colIndex = prevRow + dr,  prevCol + dc
                # print('rowIndex: ', rowIndex, 'colIndex: ', colIndex)
                if self.visited[rowIndex][colIndex]:
                    continue
                result = self.dfs(board, rowIndex, colIndex, word, wordIndex + 1)
                if result:
                    return True
            self.visited[prevRow][prevCol] = False
            return False

    def createVisited(self, board):
        nRows = len(board)
        nCols = len(board[0])
        self.visited = [[False] * (nCols + 2) for _ in range(nRows + 2)]

    def padMatrix(self, board):
        self.padCols(board)
        self.padRows(board)

    def padRows(self, board):
        nCols = len(board[0])
        newRow = [''] * nCols
        board.insert(0, newRow)
        board.append(newRow)

    def padCols(self, board):
        for row in board:
            row.insert(0, '')
            row.append('')


s = Solution()
board = [
          ['A', 'B', 'C', 'E'],
          ['S', 'F', 'C', 'S'],
          ['A', 'D', 'E', 'E']
        ]

# ['0', '0', '0', '0', '0', '0'],
# ['0', 'A', 'B', 'C', 'E', '0'],
# ['0', 'S', 'F', 'C', 'S', '0'],
# ['0', 'A', 'D', 'E', 'E', '0'],
# ['0', '0', '0', '0', '0', '0']]

board2 = [["a", "a", "a", "a"], ["a", "a", "a", "a"], ["a", "a", "a", "a"]]
word1, word2, word3, word4, word5, word6 = 'ABCCED', 'SEE', 'ABCB', 'KEDAR', 'K', 'aaaaaaaaaaaaa'
print(s.exist(board2, word6))
