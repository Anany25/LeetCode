class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:


        if sum(candies) < k:
            return 0

        lo, hi = 1, max(candies)
        ans = 0
        
        while lo <= hi:
            mid = (lo + hi) // 2
            count = 0
            for c in candies:
                count += c // mid
            
            if count >= k:
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
                
        return ans
