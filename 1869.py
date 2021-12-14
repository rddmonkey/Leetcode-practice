class Solution:
    def checkZeroOnes(self, s: str) -> bool:

        currentone,maxone,currentzero,maxzero,highone,highzero = 0,0,0,0,0,0

        for num in s:
            if num == "1":
                maxone += 1
                maxzero = 0
            if num == "0":
                maxone = 0
                maxzero += 1

            if highone < maxone:
                highone = maxone
            if highzero < maxzero:
                highzero = maxzero

        if highone > highzero:
            return True
        return False
