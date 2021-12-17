class Solution:
    def reverse(self, x: int) -> int:
        
        if x == 0:
            return 0
        ans = ""
        neg = False
        if x < 0:
            neg = True
            x = -x

        while x > 0:
            ans += str(x % 10)
            x = x // 10

        if neg:
            ans = int(ans)
            ans = -ans
        else:
            ans = int(ans)

        if ans > 2 ** 31 or ans < -2 ** 31 - 1:
            return 0

        return ans
