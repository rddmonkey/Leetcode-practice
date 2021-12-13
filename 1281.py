class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        
        nums = []
        value = 1
        
        while n > 0:
            nums.append(n%10)
            n = n //10
        
        for x in nums:
            value *= x
        
        return value - sum(nums)
