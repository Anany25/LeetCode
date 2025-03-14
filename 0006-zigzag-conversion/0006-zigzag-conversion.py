class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n = len (s)
        if numRows == 1:
            return s

        pat = [[0] * n for _ in range(n)]


        pat[0][0] = s[0]
        countdown, countup = 0, 0
        i, j = 0, 0

        for char in s[1:]:
            if countdown < numRows-1:
                i += 1

                pat[i][j] = char
                countdown +=1
                if i > numRows:
                    break
                
            elif countdown == (numRows -1) and countup <numRows -1:
                i -= 1
                j += 1
                if i > numRows:
                    break
                pat[i][j] = char
                countup +=1

            if countdown == (numRows -1) and countup == (numRows -1):
                countdown, countup = 0, 0


        ans = ""


        for i in range(0 ,len(pat)):
            for j in range(0, len(pat[0])):
                if pat[i][j] != 0:
                    ans = ans + pat[i][j]
        
        return ans