class Solution:
    def isPalindrome(self, s: str) -> bool:
        s2 = []
        for char in s:
            if char.isalnum():
                s2.append(char.lower())

        print(s2,s2[::-1])

        return s2[::-1] == s2