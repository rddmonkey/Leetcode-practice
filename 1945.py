class Solution:
    def getLucky(self, s: str, k: int) -> int:

        lettonum = ""

        for c in s:
            lettonum += str(ord(c) -96)

        while k != 0:
            lettonum = [int(x) for x in lettonum]
            total = sum((lettonum))
            lettonum = str(total)
            k -= 1

        return int("".join(lettonum))
