class Solution:
    def sortSentence(self, s: str) -> str:

        slist = s.split()

        sindices = [int(x[-1])-1 for x in slist]

        ans = [""] * len(sindices)

        for i in range(len(sindices)):
            ans[sindices[i]] = slist[i]

        solution = []

        for x in ans:
            num = x[0:len(x)-1]
            solution.append(num)

        return " ".join(solution)
