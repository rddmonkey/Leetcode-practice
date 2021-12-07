class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:

        ans = 0

        textlist = text.split()

        for word in textlist:
            length = len(word)-1
            for letter in word:
                if letter in brokenLetters:
                    break
                if length == 0:
                    ans += 1
                else:
                    length -= 1

        return ans
