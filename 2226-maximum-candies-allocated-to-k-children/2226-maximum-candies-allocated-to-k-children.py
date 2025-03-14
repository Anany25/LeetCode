class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        # Quick check: if the total candies are less than k, distribution is impossible
        if sum(candies) < k:
            return 0

        lo, hi = 1, max(candies)
        ans = 0
        
        while lo <= hi:
            mid = (lo + hi) // 2
            count = sum(c // mid for c in candies)
            
            if count >= k:
                ans = mid  # mid is a valid candidate
                lo = mid + 1  # Try for a larger number
            else:
                hi = mid - 1  # mid is too high, reduce the search space
                
        return ans
