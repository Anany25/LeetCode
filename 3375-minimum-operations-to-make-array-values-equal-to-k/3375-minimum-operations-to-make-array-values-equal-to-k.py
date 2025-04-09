class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:

        if min(nums) < k:
            return -1
        nums.sort(reverse= True)
        count = 0

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                count += 1

        if nums[-1] > k:
            count += 1
        return count
