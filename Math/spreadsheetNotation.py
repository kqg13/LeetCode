# HackerRank: Spreadsheet notation


def getSpreadsheetNotation(n):
    row = str(getRow(n))
    colIndex = getColIndex(n)
    cols = getColLetters(colIndex)
    return row + cols


def getRow(n):
    return (n // (26 * 27)) + 1


def getColIndex(n):
    return n % (26 * 27)


def getColLetters(colIndex):
    q, r = divmod(colIndex, 26)
    secondLet = chr((ord('A') - 1) + r)
    firstLet = chr(ord('A') - 1 + q) if q != 0 else ""
    return firstLet + secondLet


print(getSpreadsheetNotation(27))
