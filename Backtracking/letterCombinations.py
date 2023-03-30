# Problem 17: Letter Combinations of a Phone Number

# Given a string containing digits from 2-9 inclusive, return all possible
# letter combinations that the number could represent. Return the answer
# in any order.
#
# A mapping of digit to letters (just like on the telephone buttons) is given below.
# Note that 1 does not map to any letters.

# Examples:
# Input1:   digits1 = "23"
# Output1:  ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
# Input2:   digits2 = ""
# Output2:  []
# Input3:   digits3 = "2"
# Output3:  ["a", "b", "c"]


# Time: O(4^n), Space: O(n) where n = # of digits stack space and O(4^n) for storing strings
class Solution:
    def letterCombinations(self, digits: str):
        if not digits: return []
        self.mappings = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        currentList, results = [], []
        self.letterCombinationsHelper(digits, 0, currentList, results)
        return results

    def letterCombinationsHelper(self, digits: str, index: int, currentList: list, results: list):
        if index == len(digits):
            results.append(''.join(currentList))
            return
        for letter in self.mappings[digits[index]]:
            currentList.append(letter)
            self.letterCombinationsHelper(digits, index + 1, currentList, results)
            currentList.pop()


s = Solution()
digits1 = "23"
digits2 = ""
digits3 = "2"
print(s.letterCombinations(digits2))
