class Solution:
    def countGoodSubstrings(self, s: str) -> int:

        ans = 0

        for i in range(len(s)):
            if len(set(s[i:i+3])) == 3:
                ans += 1

        return ans
