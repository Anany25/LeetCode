class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        nums = []
        base_remainder = grid[0][0] % x
        
        for row in grid:
            for val in row:
                if val % x != base_remainder:
                    return -1
                nums.append(val)
        
        nums.sort()
        median = nums[len(nums) // 2]
        
        return sum(abs(num - median) // x for num in nums)