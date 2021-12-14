class Solution:
    def sortSentence(self, s: str) -> str:

        words = s[::-1].split()
        words.sort()

        for i in range(len(words)):
            words[i] = words[i][::-1][0:len(words[i])-1]

        return " ".join(words)
