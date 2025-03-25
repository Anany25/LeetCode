class Solution:
    def trap(self, height: List[int]) -> int:
        i = 0
        j = 1
        ans = 0
        maxi = 0
        for k in range(len(height)):
            if height[k] >= height[maxi]:
                maxi = k

        while j < maxi:
            if height[i]>= height[j]:
                ans += (height[i] - height[j])
                j += 1
            elif height[i] < height[j]:
                i = j 
                j = i + 1

        
        i , j= len(height) - 1, len(height) - 2
        print("abc")
        while j > maxi:
            if height[i] >= height[j]:
                ans += (height[i] - height[j])
                j -= 1
            elif height[i] < height[j]:
                i = j 
                j = i - 1

        return ans

