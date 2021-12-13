class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:

        count = 0
        letters = []

        for x in text:
            if x in "balloon":
                letters.append(x)

        while True:
            for l in "balloon":
                if l in letters:
                    letters.remove(l)
                    if l == "n":
                        count +=1
                else:
                    return count
