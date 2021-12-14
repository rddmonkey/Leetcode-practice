class Solution:
    def sortSentence(self, s: str) -> str:

        slist = s.split()

        sindices = [int(x[-1])-1 for x in slist]

        ans = [""] * len(sindices)

        for i in range(len(sindices)):
            ans[sindices[i]] = slist[i][0:len(slist[i])-1]

        return " ".join(ans)
