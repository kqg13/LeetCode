# 244: Shortest Word Distance II
# https://leetcode.com/problems/shortest-word-distance-ii/description/?envType=problem-list-v2&envId=hash-table


from typing import List
from collections import defaultdict


class WordDistance:
    def __init__(self, wordsDict: List[str]):
        self.locations_dict = defaultdict(list)

        for i, word in enumerate(wordsDict):
            self.locations_dict[word].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        word1_locs = self.locations_dict[word1]
        word2_locs = self.locations_dict[word2]
        n_word1_locs, n_word2_locs = len(word1_locs), len(word2_locs)
        result = float('inf')
        i = j = 0
        while i < n_word1_locs and j < n_word2_locs:
            index_i, index_j = word1_locs[i], word2_locs[j]
            result = min(result, abs(index_j - index_i))
            if result == 1:
                break
            if index_i < index_j:
                i += 1
            else:
                j += 1

        return result


word_list = ["practice", "makes", "perfect", "coding", "makes"]
wl = WordDistance(word_list).shortest("makes", "coding")
