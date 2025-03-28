from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        d1, d2 = defaultdict(int), defaultdict(int)

        for char in s1:
            d1[char] += 1

        left = 0
        for right in range(len(s2)):
            d2[s2[right]] += 1

            if right - left + 1 > len(s1):
                if d2[s2[left]] == 1:
                    del d2[s2[left]]
                else:
                    d2[s2[left]] -= 1
                left += 1

            if d1 == d2:
                return True

        return False
