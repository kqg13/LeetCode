# 299: Bulls and Cows
# https://leetcode.com/problems/bulls-and-cows/

from collections import defaultdict


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = cows = 0
        d_secret = defaultdict(lambda: 0)
        d_guess = defaultdict(lambda: 0)

        for i in range(len(guess)):
            s, g = secret[i], guess[i]
            if s == g:
                bulls += 1
            else:
                c_secret = d_guess.get(s, 0)
                if c_secret == 0:
                    d_secret[s] += 1
                else:
                    cows += 1
                    d_guess[s] -= 1

                c_guess = d_secret.get(g, 0)
                if c_guess == 0:
                    d_guess[g] += 1
                else:
                    cows += 1
                    d_secret[g] -= 1

        str_bulls, str_cows = str(bulls), str(cows)
        result = "%sA%sB" % (str_bulls, str_cows)

        return result


s = Solution()
secret1, guess1 = "1807", "7810"   # Expected: 1A3B
secret2, guess2 = "1123", "0111"  # Expected: 1A1B
secret3, guess3 = "1122", "2211"  # Expected: 0A4B
