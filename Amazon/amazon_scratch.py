from statistics import median
from math import ceil
from itertools import combinations
from collections import defaultdict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x=None):
        self.val = x
        self.left = None
        self.right = None


def makeBST(values):
    """
    Constructs BST given list of n unique ints without rebalancing the tree
    :param values: List[int]
    :return: TreeNode
    """
    if values is None: return None
    root = TreeNode(values[0])
    for i in range(1, len(values)):
        val_to_insert = values[i]
        root = insertNode(root, val_to_insert)
    print(root.val, root.left.val, root.right.val, root.left.left.val, root.left.right.val, root.left.left.right.val)


def insertNode(node, val_to_insert):
    if node is None:
        return TreeNode(val_to_insert)
    if val_to_insert < node.val:
        node.left = insertNode(node.left, val_to_insert)
    elif val_to_insert > node.val:
        node.right = insertNode(node.right, val_to_insert)
    return node


def maximumQuality(packets, channels):
    # Sort
    packets_sorted = sorted(packets)
    # Greedy: highest channels get their separate channels
    channels_less_one = channels - 1
    single_channels = sum(packets_sorted[-channels_less_one:])
    # Get median of multi-channels
    multi_channel_bound = len(packets) - channels_less_one
    multi_channels = int(ceil(median(packets_sorted[:multi_channel_bound])))
    return single_channels + multi_channels


def maxDifference(px):
    n = len(px)
    if n == 1:
        return -1
    greatest_delta, curr_min = 0, px[0]
    for i in range(1, n):
        # find min of pxs such that their index <= i
        curr_min = min(px[i], curr_min)
        # if a new minimum is found:
        #    px[i] - curr_min = 0 since px[i] - px[i] = 0
        # else: (i < j is implied)
        #    take max of greatest and px[i] - curr_min
        greatest_delta = max(px[i] - curr_min, greatest_delta)
    return greatest_delta if greatest_delta > 0 else -1


def rearrange(arr):
    results = list()
    sorted_arr = sorted(arr)
    n = len(sorted_arr)
    if n < 3:
        return sorted_arr
    j, k = (n - 1) // 2, 0
    print(k)
    results.append(sorted_arr[j])
    j += 1
    results.append(sorted_arr[j])
    j += 1
    for i in range(2, n):
        if i % 2 == 0:
            results.append(sorted_arr[k])
            k += 1
        else:
            results.append(sorted_arr[j])
            j += 1
    return results


def uniqueLetterString(s):
    if not s:
        return 0
    left = list()
    the_map = dict()
    for i in range(len(s)):
        c = s[i]
        if c not in the_map:
            the_map[c] = -1
        left.insert(i, the_map[c])
        the_map[c] = i


# Amazon OA: SDE2
# Find the strength a password per the definition of strength mentioned below
# The strength of a pw is the sum of all the unique characters in all the
# possible substrings of a word.
#
# e.g password is "test"
# possible substrings are -> "t","e","s","t", "te","es","st", "tes", "est", "test"
# here the strength is 1 + 1 + 1 + 1+ 2+ 2 + 2 + 3 + 3 + 3 = 19
# e.g. password is "good" ---> 16


# Submitted approach failed 4 test cases due to out of memory error
# Excessive space
def findPasswordStrength(password):
    all_substrings = {password[x:y] for x, y in combinations(range(len(password) + 1), r=2)}
    print(all_substrings)
    strength = 0
    for word in all_substrings:
        set_string = set(word)
        strength += len(set_string)
    return strength


# Better approach
def findPassWordStrengthDP(password):
    n = len(password)
    result = n
    matrix = [[0]*n for _ in range(n)]
    matrix[0] = [1] * n
    for i in range(1, n):
        for j in range(i, n):
            isIncrement = 0 if password[j] == password[j - i] else 1
            matrix[i][j] = min(matrix[i-1][j], matrix[i-1][j-1]) + isIncrement
            result += matrix[i][j]
    return result


# Another approach posted on LC Discussions
def strength_pwd(s: str):
    dic = defaultdict(lambda: (0, 0))
    prev = 0
    ans = 0
    for i, ch in enumerate(s):
        cur = prev+i+1
        dic[ch] = (i + 1, dic[ch][1] + dic[ch][0])
        ans += cur - sum([dic[k][1] for k in dic])
        prev = cur
    return ans


def findMedianSortedArrays(nums1, nums2):
    """
    :param nums1: list[int]
    :param nums2: list[int]
    :return: float
    """
    pass


def isHappy(n: int) -> bool:
    if n == 1:
        return True
    s = {n}
    while True:
        n_str = str(n)
        total = 0
        for c in n_str:
            total += int(c) ** 2
        print("total: ", total)
        if total == 1:
            return True
        if total in s:
            break
        s.add(total)
        n = total
    print("set: ", s)
    return False


print(isHappy(6))
# nums1, nums2 = [1, 2, 3], [4, 5, 6]
# findMedianSortedArrays(nums1, nums2)
#
# print(uniqueLetterString('Leetcode'))
# arr1 = [5, 9, 7, 34, 21]
# arr2 = [5, 7, 9, 21]
# arr3 = [1, 2, 3]
# print(rearrange(arr3))

# px1 = [7, 1, 2, 5]
# px2 = [7, 5, 3, 1]
# px3 = [4, 3, 2, 1]
# px4 = [1, 2, 6, 4]
# px5 = [7, 9, 5, 6, 3, 2]
# px6 = [2, 3, 10, 2, 4, 8, 1]


# packets1 = [3, 1, 5, 4, 2]  # [1, 2, 3, 4, 5]
# print(maximumQuality(packets1, 2))
# packets2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(maximumQuality(packets2, 4))

# tree_vals = [5, 6, 3, 1, 2, 4]
# makeBST(tree_vals)
# print(t.val, t.left.val, t.right.val, t.left.left.val, t.left.right.val, t.left.left.right.val)
