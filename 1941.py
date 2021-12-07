class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:

        mydict = {}

        for x in s:
            if x not in mydict:
                mydict[x] = 1
            else:
                mydict[x] += 1

        maxfreq = max(mydict.values())

        for k,v in mydict.items():
            if v != maxfreq:
                return False
        return True
