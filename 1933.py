class Solution:
    def isDecomposable(self, s: str) -> bool:

        stack = []
        numbers = []
        possible3 = True

        for i in range(len(s)):
            if len(stack) == 0:
                stack.append(s[i])
                if i == len(s) -1 and len(stack) == 1:
                    return False
                continue
            if s[i] == stack[-1]:
                stack.append(s[i])
                if i == len(s) -1 and len(stack) == 3:
                    numbers.append(3)
                if i == len(s) -1 and len(stack) > 3:
                    possible3 = False
                    if len(stack) % 3 == 0:
                        numbers.append(3)
                        break
                    if len(stack) % 3 == 1:
                        return False
                    if len(stack) % 3 == 2:
                        if 2 not in numbers:
                            numbers.append(3)
                            numbers.append(2)
                        else:
                            return False
                if i == len(s) - 1 and len(stack) == 2:
                    print(stack)
                    if 2 not in numbers:
                        numbers.append(2)
                    else:
                        return False
                continue
            if s[i] != stack[-1]:
                if len(stack) == 1:
                    return False
                if len(stack) >= 3:
                    possible3 = False
                    if len(stack) % 3 == 0:
                        numbers.append(3)
                        stack = [s[i]]
                        continue
                    if len(stack) % 3 == 1:
                        return False
                    if len(stack) %3 == 2:
                        if 2 not in numbers:
                            numbers.append(3)
                            numbers.append(2)
                            stack = [s[i]]
                        else:
                            return False
            if len(stack) == 1:
                stack = [s[i]]
                continue
            if len(stack) == 2:
                if 2 not in numbers:
                    numbers.append(2)
                    stack = [s[i]]
                    if i == len(s) -1 and len(stack) == 1:
                        return False
                else:
                    return False


        if numbers.count(2) == 1 and possible3 == True:
            return True
        if len(set(numbers)) ==2:
            return True

        return False
