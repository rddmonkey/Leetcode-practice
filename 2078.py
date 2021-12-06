class Solution:
    def maxDistance(self, colors) -> int:

        possible = []
        ipossible = []
        hdistance = 0
        start = 0

        for num in range(len(colors)):
            if colors[num] not in possible:
                possible.append(colors[num])
                ipossible.append(num)

        while start < len(possible):
            for i in range(len(colors)-1,-1,-1):
                if colors[i] != possible[start]:

                    distance = i -ipossible[start]
                    if distance > hdistance:
                        hdistance = distance
                        break
                    else:
                        break
            start += 1

        return hdistance
