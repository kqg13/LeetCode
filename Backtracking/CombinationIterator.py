# LeetCode Problem 1286: Iterator for Combination

# Design an Iterator class, which has:
# - A constructor that takes a string chars of sorted distinct LC English letters and a # combinationLength as args.
# - A function next() that returns the next combo of length combinationLength in lexicographical order.
# - A function hasNext() that returns True iff there exists a next combo.

# Example:
# CombinationIterator iterator = new CombinationIterator("abc", 2); // creates the iterator.
# iterator.next(); // returns "ab"
# iterator.hasNext(); // returns true
# iterator.next(); // returns "ac"
# iterator.hasNext(); // returns true
# iterator.next(); // returns "bc"
# iterator.hasNext(); // returns false

# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()


class CombinationIterator:
    def __init__(self, characters: str, combinationLength: int):
        self.characters = characters
        self.combinationLength = combinationLength

        self.combinations = []
        self.n = len(characters)

        self.backtrack([], 0)
        self.combinations.reverse()

    def backtrack(self, current, letter):
        if len(current) == self.combinationLength:
            self.combinations.append(''.join(current.copy()))
            return
        for i in range(letter, self.n):
            current.append(self.characters[i])
            self.backtrack(current, i + 1)
            current.pop()

    def next(self) -> str:
        return self.combinations.pop()

    def hasNext(self) -> bool:
        return len(self.combinations) != 0


str1, comboLength1 = "abc", 2
comboIter = CombinationIterator(str1, comboLength1)
