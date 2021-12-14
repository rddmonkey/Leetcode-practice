class Solution:
    def maxProductDifference(self, nums) -> int:
        nums.sort()

        multhigh = nums[-1] * nums[-2]
        multlow = nums[0] * nums[1]

        return multhigh - multlow
