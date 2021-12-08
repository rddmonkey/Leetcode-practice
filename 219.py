class Solution:
    def containsNearbyDuplicate(self, nums, k: int) -> bool:

        start = 0

        while start != len(nums) -1:
            for i in range(len(nums)):
                if i == start:
                    continue
                if nums[start] == nums[i]:
                    if abs(start-i) <= k:
                        return True
            start += 1

        return False
