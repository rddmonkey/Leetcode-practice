class Solution:
    def minDeletionSize(self, strs) -> int:

        indexstart = 0
        ans = 0

        while indexstart != len(strs[0]):
            start = 0
            stack = []
            while start != len(strs):
                if start == 0:
                    stack.append(strs[start][indexstart])
                if strs[start][indexstart] == stack[-1]:
                    start += 1
                    continue
                if strs[start][indexstart] < stack[-1]:
                    ans += 1
                    break
                else:
                    stack.pop()
                    stack.append(strs[start][indexstart])

                start += 1
            indexstart += 1

        return ans
