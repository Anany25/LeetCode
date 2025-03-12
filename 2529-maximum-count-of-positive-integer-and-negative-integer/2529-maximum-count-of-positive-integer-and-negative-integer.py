class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        n = len(nums)
        
        lo, hi = 0, n
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] < 0:
                lo = mid + 1
            else:
                hi = mid
        countNeg = lo
        
        lo, hi = 0, n
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] <= 0:
                lo = mid + 1
            else:
                hi = mid
        countPos = n - lo
        
        return max(countNeg, countPos)