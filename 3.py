class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = float('-inf')
        start = 0
        stacked = False

        while start != len(s):
            stack = []
            for i in range(start,len(s)):
                if not stack:
                    stacked = True
                    stack.append(s[i])
                    if i == len(s) - 1:
                        if len(stack) > longest:
                            longest = len(stack)
                    continue
                if s[i] in stack:
                    if len(stack) > longest:
                        longest = len(stack)
                    break
                else:
                    stack.append(s[i])
                    if i == len(s) - 1:
                        if len(stack) > longest:
                            longest = len(stack)
            start += 1


        if stacked == False:
            return 0

        return longest
