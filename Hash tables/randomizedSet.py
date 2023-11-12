# 380 - Insert Delete Get Random O(1)
# https://leetcode.com/problems/insert-delete-getrandom-o1/?envType=study-plan-v2&envId=top-interview-150

import random


class RandomizedSet:
    def __init__(self):
        self.index_to_val = dict()
        self.val_to_index = dict()
        self.n = 0

    def insert(self, val: int) -> bool:
        if val in self.val_to_index: return False
        self.n += 1
        self.val_to_index[val] = self.n
        self.index_to_val[self.n] = val
        return True

    def remove(self, val: int) -> bool:
        if val not in self.val_to_index: return False
        index_to_remove = self.val_to_index[val]
        val_to_move = self.index_to_val[self.n]
        self.val_to_index[val_to_move] = index_to_remove
        del self.val_to_index[val]

        self.index_to_val[index_to_remove] = val_to_move
        del self.index_to_val[self.n]
        self.n -= 1
        return True

    def getRandom(self) -> int:
        rand_n = random.randint(1, self.n)
        return self.index_to_val[rand_n]
