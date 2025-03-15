class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        
        left, right = min(nums), max(nums)
        n = len(nums)
        mini = right
        

        def can_rob(x : int):
            count = 0
            i = 0

            while i < n:
                if nums[i] <= x:
                    count +=1
                    i += 2
                else:
                    i += 1 
                if count == k:
                    return True

            return False

        while left <= right:
            mid = (left + right) // 2
            if can_rob(mid):
                mini = mid
                right = mid - 1
            else:
                left = mid + 1
                
        return mini