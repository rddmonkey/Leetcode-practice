class Solution:
    def uniqueOccurrences(self, arr) -> bool:
        mydict = {}

        for x in arr:
            if x not in mydict:
                mydict[x] = 1
            else:
                mydict[x] += 1


        return sorted(list(mydict.values())) == sorted(list(set(mydict.values())))
