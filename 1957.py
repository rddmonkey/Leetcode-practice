class Solution:
    def makeFancyString(self, s: str) -> str:

        count = 0
        ans = ""

        for i,c in enumerate(s):
            if i > 0 and c == s[i-1]:
                count += 1
            else:
                count = 1
            if count < 3:
                ans += c

        return ans
