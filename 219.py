class Solution:
    def containsNearbyDuplicate(self, nums, k: int) -> bool:

        dic = {}
        for i, v in enumerate(nums):
            if v in dic and i - dic[v] <= k:

                return True
            dic[v] = i
        return False
