class Solution:
    def relativeSortArray(self, arr1, arr2):

        mydict = {}
        notin = []

        for x in arr1:
            if x not in arr2:
                notin.append(x)
        notin.sort()

        for x in arr1:
            if x not in mydict:
                mydict[x] = 1
            else:
                mydict[x] += 1

        ans = []

        for num in arr2:
            ans.extend([num]*mydict.get(num))

        ans.extend(notin)

        return ans
