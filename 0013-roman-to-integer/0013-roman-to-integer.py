class Solution:
    def romanToInt(self, s: str) -> int:
        num = list(s)

        total = 0
        prev = None 

        for i in range(len(num)):
            if num[i] == 'M':
                if (prev == 'C'):
                    total += 800
                else:
                    total += 1000
                prev = "M"
            elif num[i] == 'D':
                if (prev== 'C'):
                    total += 300
                else:
                    total += 500
                prev = 'D'
            elif num[i] == 'C':
                if (prev== 'X'):
                    total += 80
                else:
                    total += 100
                prev = 'C'
            elif num[i] == 'L':
                if (prev== 'X'):
                    total += 30
                else:
                    total += 50
                prev = 'L'
            elif num[i] == 'X':
                if (prev== 'I'):
                    total += 8
                else:
                    total += 10
                prev = 'X'
            elif num[i] == 'V':
                if (prev== 'I'):
                    total += 3
                else:
                    total += 5
                prev = 'V'
            elif num[i] == 'I':
                total += 1
                prev = 'I'

        return total