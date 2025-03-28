class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d1 , d2 = defaultdict(int), defaultdict(int)

        for char in s1:
            d1[char] += 1

        n = len(s1)
        m = len(s2)

        left = 0

        right = n

        while right <= m:
            
            for char in range(left,right):
                d2[s2[char]] += 1
    
            if d1== d2:
                return True

            else:
                d2.clear()
                left += 1
                right += 1

        return False
            