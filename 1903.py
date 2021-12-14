class Solution:
    def largestOddNumber(self, num: str) -> str:
        number = num

        if int(num) % 2 == 1:
            return num

        while int(num) > 0:
            num = int(num) // 10
            if int(num) % 2 == 1:
                return str(num)

        possible = [int(x) for x in number if int(x) % 2 ==1]


        if len(possible) >0:
            return max(str(possible))
        else:
            return ""
