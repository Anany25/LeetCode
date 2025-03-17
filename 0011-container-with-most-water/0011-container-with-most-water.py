class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        i = 0
        j = n -1
        ans = 0
        while i < j:
            vol = min(height[i],height[j]) * (j - i)
            ans = max (ans, vol)
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1

        return ans  


