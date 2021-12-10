class Solution:
    def isAlienSorted(self, words, order: str) -> bool:

        aliendict = {}

        for i, v in enumerate(order):
            aliendict[v] = i

        for i in range(len(words)-1):
            for j in range(len(words[i])):
                if j >= len(words[i+1]):
                    return False
                if words[i][j] != words[i+1][j]:
                    if aliendict[words[i][j]] > aliendict[words[i+1][j]]:
                        return False
                    break
        return True
