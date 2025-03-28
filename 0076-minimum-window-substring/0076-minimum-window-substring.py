class Solution:
    def minWindow(self, s: str, t: str) -> str:
        d1, d2 = defaultdict(int), defaultdict(int)

        for char in t:
            d1[char] += 1

        required = len(d1)
        formed = 0

        left = 0
        min_len = float('inf')
        min_window = ""

        for right in range(len(s)):
            d2[s[right]] += 1

            if s[right] in d1 and d2[s[right]] == d1[s[right]]:
                formed += 1

            while left <= right and formed == required:
                if (right - left + 1) < min_len:
                    min_len = right - left + 1
                    min_window = s[left: right + 1]
                
                d2[s[left]] -= 1
                if s[left] in d1 and d2[s[left]] < d1[s[left]]:
                    formed -= 1

                left += 1

        return min_window
