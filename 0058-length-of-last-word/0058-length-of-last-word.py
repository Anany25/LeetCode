class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        maxi = len(s)
        if maxi == 0:
            return 0
        n = maxi -1
        length = 0
        while n>= 0:
            if s[n] == " " and length >0:
                return length
            elif s[n] != " ":
                length += 1
            n -= 1
        return length   