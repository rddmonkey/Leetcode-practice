import string

class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:

        mydict = {}
        abcs = string.ascii_lowercase
        firstpoints = ""
        secondpoints = ""
        targetpoints = ""

        for i in range(len(abcs)):
            mydict[abcs[i]] = i

        for x in firstWord:
            for k, v in mydict.items():
                if x == k:
                    firstpoints += str(v)

        for x in secondWord:
            for k, v in mydict.items():
                if x == k:
                    secondpoints += str(v)

        for x in targetWord:
            for k, v in mydict.items():
                if x == k:

                    targetpoints += str(v)

        return int(firstpoints) + int(secondpoints) == int(targetpoints)
