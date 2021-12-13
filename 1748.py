class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        
        mydict = {}
        
        for x in nums:
            if x not in mydict:
                mydict[x] = 1
            else:
                mydict[x] += 1 
        
        ans = []
        
        for k, v in mydict.items():
            if v == 1:
                ans.append(k)
        return sum(ans)
