class Solution:
    def restoreString(self, s: str, indices) -> str:
        ans = [0] * len(s)

        for i in range(len(indices)):
            ans[indices[i]] = s[i]

        return "".join(ans)
