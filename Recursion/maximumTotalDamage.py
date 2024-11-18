# 3186: Maximum Total Damage With Spell Casting
# https://leetcode.com/problems/maximum-total-damage-with-spell-casting/?envType=company&envId=citadel&favoriteSlug=citadel-six-months

from collections import Counter


class Solution(object):
    def maximumTotalDamage(self, power):
        """
        :type power: List[int]
        :rtype: int
        """
        cnt = Counter(power)
        m = len(cnt) + 1
        dp = [[0] * m for _ in range(2)]

        sorted_cnt = sorted(map(int, cnt.keys()))
        # bound
        sorted_cnt.insert(0, 0)

        for i, num in enumerate(sorted_cnt[1:], 1):
            # don't take row
            dp[1][i] = max(dp[0][i - 1], dp[1][i - 1])
            # take row
            lookback = max(num - 3, 0)

            j = 1
            while True:
                if sorted_cnt[i - j] <= lookback:
                    break
                j += 1
            # get dp value
            current_val = cnt[num] * num
            dp[0][i] = max(dp[0][i - j], dp[1][i - j]) + current_val

        ans = max(dp[0][-1], dp[1][-1])

        return ans


s = Solution()
power1 = [1, 1, 3, 4]  # Expected: 6
power2 = [7, 1, 6, 6]  # Expected: 13
s.maximumTotalDamage(power2)
