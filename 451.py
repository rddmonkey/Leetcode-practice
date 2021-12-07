class Solution:
    def frequencySort(self, s: str) -> str:

        mydict = {}
        ans = []


        for letter in s:
            if letter not in mydict:
                mydict[letter] = 1
            else:
                mydict[letter] += 1

        maxfreq = max(mydict.values())

        while maxfreq > 0:

            for k, v in mydict.items():
                if v == maxfreq:
                    ans.extend([k]*v)
            maxfreq -= 1


        return "".join(ans)
