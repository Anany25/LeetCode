class Solution:
    def longestPalindrome(self, s: str) -> str:
        def isPal(x):
            rev_x = x[::-1]
            if x == rev_x:
                return True
            return False

        if len(s) <= 1:
            return s

        maxi = 0
        lp = ""
        for i in range (0, len(s)-1):
            for j in range (i, len(s)):
                if j-i+1 > maxi and s[i:j+1] == s[i:j+1][::-1]:
                    
                        lp = s[i: j + 1]
                        maxi = j - i + 1

        return lp