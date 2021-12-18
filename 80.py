class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        mydict = {}
        
        count = 0
        length = len(nums)
        
        for x in nums:
            if x not in mydict:
                mydict[x] = 1
            else:
                mydict[x] += 1
        
        for x in set(nums):
            while mydict[x] > 2:
                nums.remove(x)
                mydict[x] -=1
                count += 1
                
        return length - count
