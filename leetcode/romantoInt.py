class Solution:
    def romanToInt(self, s: str) -> int:
        index = 0
        total = 0
        self.s = s
        summation = []
        for i in self.s:
            if i == "I":
                if (index + 1) < len(self.s):
                    if s[index + 1] == "V" or s[index + 1] == "X":
                        summation.append(-1)
                        total += -1
                    else:
                        summation.append(1)
                        total += 1
                else:
                    summation.append(1)
                    total += 1
            if i == "V":
                summation.append(5)
                total += 5
            if i == "X":
                if (index + 1) < len(self.s):
                    if s[index + 1] == "L" or s[index + 1] == "C":
                        summation.append(-10)
                        total += -10
                    else:
                        summation.append(10)
                        total += 10
                else:
                    summation.append(10)
                    total += 10
            if i == "L":
                summation.append(50)
                total += 50
            if i == "C":
                if (index + 1) < len(self.s):
                    if s[index + 1] == "D" or s[index + 1] == "M":
                        summation.append(-100)
                        total += -100
                    else:
                        summation.append(100)
                        total += 100
                else:
                    summation.append(100)
                    total += 100
            if i == "D":
                summation.append(500)
                total += 500
            if i == "M":
                summation.append(1000)
                total += 1000
            index += 1
        return total
