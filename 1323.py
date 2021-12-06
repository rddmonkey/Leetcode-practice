class Solution:
    def maximum69Number (self, num: int) -> int:

        num = str(num)
        ans = [x for x in num]

        for i in range(len(ans)):
            if ans[i] == "6":
                ans[i] = "9"
                break

        return "".join(ans)
