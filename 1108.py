class Solution:
    def defangIPaddr(self, address: str) -> str:

        ans = ""

        for x in address:
            if x == ".":
                ans += "[.]"
            else:
                ans += x

        return ans
