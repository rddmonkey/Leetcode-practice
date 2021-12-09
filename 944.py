class Solution:
    def minDeletionSize(self, strs) -> int:

        ans = 0

        for c in zip(*strs):
            if list(c) != sorted(c):
                ans += 1
        return ans
