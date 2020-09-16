# String problem 49: Group Anagrams

# Given an array of strings strs, group the anagrams together. Return the answer in any order.

# Ex 1: Input: strs = ["eat", "tea", "tan", "ate", "nat", "bat"],
#       Output: [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]

# Ex 2: Input: strs = [""], Output: [[""]]

# Ex 3: Input: strs = ["a"], Output: [["a"]]


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # Alphabetize the inputs
        sortedList = []
        for i, word in enumerate(strs):
            sorted_strs = "".join(sorted(word))
            sortedList.append(sorted_strs)
            del sorted_strs
        # Group in dictionary
        thisDict = {}
        for i, word in enumerate(sortedList):
            if word not in thisDict:
                thisDict[word] = [strs[i]]
            else:
                thisDict[word].append(strs[i])
        # Loop through dictionary
        results = []
        for lst in thisDict.values():
            results.append(lst)
        return results
