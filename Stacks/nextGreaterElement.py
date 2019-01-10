# Easy problem 496: Next Greater Element I


class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        stack = []
        results = {}

        for num in nums2:
            while stack and stack[-1] < num:
                v = stack.pop()
                results[v] = num
            stack.append(num)

        for num in stack:
            results[num] = -1

        output = []
        for num in nums1:
            output.append(results[num])

        return output
