class Solution:
    def numDifferentIntegers(self, word: str) -> int:

        number = ""

        wordlist = []

        for x in word:
            if x.isnumeric():
                number += x
            if x.isnumeric() == False:
                if number != "":
                    wordlist.append(int(number))
                number = ""

        if number != "":
            wordlist.append(int(number))


        return len(set(wordlist))
