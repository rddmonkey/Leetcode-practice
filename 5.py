class Solution:
    def longestPalindrome(self, s: str) -> str:

        left = 0
        longest = 0
        ans = ""
        end = len(s) -1
        palind = False

        while left != end:
            right = len(s) - 1
            while right > left:
                if s[left] == s[right]:
                    if s[left:right+1] == s[left:right+1][::-1]:
                        palind = True
                        if len(s[left:right+1]) > longest:
                            longest = len(s[left:right+1])
                            ans = s[left:right+1]
                            break
                    right -= 1
                else:

                    right -= 1

            left += 1

        if not palind:
            return s[0]

        return ans
