class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        maxi = 1

        left = 0
        bits = 0

        for right in range(n):
            while bits & nums[right] !=  0:
                bits ^= nums[left]
                left += 1

            bits |= nums[right]

            maxi = max(maxi, right-left + 1)

        
        return maxi