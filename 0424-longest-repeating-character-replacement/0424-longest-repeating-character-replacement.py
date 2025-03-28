class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        left = 0
        maxi = 0
        ans = 0


        for right in range(len(s)):
            count[s[right]] += 1
            maxi = max(maxi,count[s[right]])

            if (right - left + 1) - maxi > k:
                count[s[left]]  -= 1
                left += 1

            ans = max(ans, right - left + 1)
            
        return ans
