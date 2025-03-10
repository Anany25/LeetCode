class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = str(x)
        lis = list(num)
        n = len(lis)
        if n == 1:
            return True
        mid = n//2
        for i in range (mid):
            if lis[i] != lis[n-1-i]:
                return False
        return True 
