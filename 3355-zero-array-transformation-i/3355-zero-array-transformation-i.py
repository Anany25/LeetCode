class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        
        n = len(nums)
        cum = [0] * n

        for x in queries:
            cum[x[0]] += 1

            if x[1] + 1 < n:
                cum[x[1] + 1] -=1

        cur = 0

        for i in range(n):
            cur += cum[i]
            if cur < nums[i]:
                return False
    

        return True
            