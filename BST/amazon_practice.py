from collections import defaultdict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x=None):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def makeBST(self, values, n, node1, node2):
        """
        Constructs BST given list of n unique ints without rebalancing the tree
        :param values: List[int]
        :param n: int
        :param node1: int
        :param node2: int
        :return: TreeNode
        """
        if n == 0:
            return None
        root = TreeNode(values[0])
        for i in range(1, n):
            val_to_insert = values[i]
            root = self.insertNode(root, val_to_insert)
        path1 = self.getPath(root, "", node1)
        print(path1)
        path2 = self.getPath(root, "", node2)
        print(path2)
        if path1 == -1 or path2 == -1:
            return -1
        return self.calcDistance(path1, path2)

    def calcDistance(self, path1, path2):
        n1, n2 = len(path1), len(path2)
        minString = min(n1, n2)
        diff = minString
        for i in range(minString):
            if path1[i] != path2[i]:
                diff = i
                break
        distance = (n2 - diff) + (n1 - diff)
        return distance

    def insertNode(self, node, node_val):
        if node is None:
            node = TreeNode(node_val)
            return node
        if node_val < node.val:
            node.left = self.insertNode(node.left, node_val)
        elif node_val > node.val:
            node.right = self.insertNode(node.right, node_val)
        return node

    def getPath(self, root, path, target):
        if root is None:
            return -1
        if root.val == target:
            return path
        if root.val > target:
            path = self.getPath(root.left, path + "0", target)
        if root.val < target:
            path = self.getPath(root.right, path + "1", target)
        return path

    # Time: O(len(inputString) * N) or O(N * k) where k = length of substrings
    def wordGame(self, inputString, N):
        """
        :param inputString: string
        :param N: int
        :return: List[string]
        """
        # freq_dict = defaultdict(int, {c: 0 for c in inputString})
        n_input = len(inputString)
        if N == 0 or N == 1 or N > n_input:
            return list()
        right_bound = n_input - N + 1
        results = list()
        for i in range(right_bound):
            freq_dict = defaultdict(lambda: 0)
            current_string = ""

            for j in range(i, i + N):
                freq_dict[inputString[j]] += 1
                current_string += inputString[j]

            if len(freq_dict) == N - 1:
                results.append(current_string)
        return results

    def resetDict(self, freq_dict):
        freq_dict.update({}.fromkeys(freq_dict, 0))

    def isAnyDuplicate(self, freq_dict):
        return any([True for k, v in freq_dict.items() if v == 2])


s = Solution()
tree_vals = [5, 6, 3, 1, 2, 4]
s.makeBST(tree_vals, 6, 2, 4)
# string1 = "awaglk"
# string2 = "xyzxmnno"
# s.wordGame(string1, 4)
# s.wordGame(string2, 3)
