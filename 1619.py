class Solution:
    def trimMean(self, arr):
        fivepercent = len(arr)*0.05
        arr.sort()

        fivepercent = int(fivepercent)

        return sum(arr[fivepercent:len(arr)-fivepercent])/len(arr[fivepercent:len(arr)-fivepercent])

