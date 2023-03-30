# 739: Daily Temperatures


# https://leetcode.com/problems/daily-temperatures/
# Given an array of ints temperatures represents the daily temperatures, return an arr such that answer[i]
# is the # of days you have to wait after the ith day to get a warmer temp.
# If there is no future day for which this is possible, keep answer[i] == 0 instead.


class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        highestSoFar = (0, temperatures[0])
        n = len(temperatures)
        results, stack = [0] * n, []
        for i, temp in enumerate(temperatures[1:], 1):
            hsfIndex, hsfTemp = highestSoFar
            if temp > hsfTemp:
                resultIndex = i - hsfIndex
                highestSoFar = (i, temp)
                results[hsfIndex] = resultIndex
                while stack:
                    iStack, iTemp = stack.pop()
                    results[iStack] = i - iStack
            else:
                while stack:
                    iStack, iTemp = stack[-1]
                    if temp > iTemp:
                        stack.pop()
                        results[iStack] = i - iStack
                    else:
                        break
                stack.append((i, temp))
        return results


temps1 = [73, 74, 75, 71, 69, 72, 76, 73]
temps2 = [30, 40, 50, 60]
temps3 = [1, 1, 0]
s = Solution()
s.dailyTemperatures(temps1)
