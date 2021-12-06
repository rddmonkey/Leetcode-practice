class Solution:
    def checkIfExist(self, arr) -> bool:

        for i in range(len(arr)):
            if arr[i] * 2 in arr:
                if arr[i] == 0:
                    if arr.count(0)> 1:
                        return True
                else:
                    return True
