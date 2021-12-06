class Solution:
    def shuffle(self, nums, n: int):

        firsthalf = nums[n:]
        secondhalf = nums[:n]

        ans = []
        start = 0

        while start != n:
            ans.append(secondhalf[start])
            ans.append(firsthalf[start])
            start += 1

        return ans
