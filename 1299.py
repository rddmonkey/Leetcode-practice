class Solution:
    def replaceElements(self, arr):

        ans = []

        for i in range(len(arr)):
            if i == len(arr) - 1:
                ans.append(-1)
                break
            ans.append(max(arr[i+1:]))

        return ans
