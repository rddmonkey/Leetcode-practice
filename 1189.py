class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:

        bcount, acount, lcount,ocount,ncount = 0,0,0,0,0

        for x in text:
            if x == "b":
                bcount += 1
            if x == "a":
                acount +=1
            if x == "l":
                lcount += 1
            if x == "o":
                ocount += 1
            if x == "n":
                ncount += 1

        ocount = ocount//2
        lcount = lcount//2

        return min(bcount,acount,lcount,ocount,ncount)
