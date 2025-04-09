class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:

        if min(nums) < k:
            return -1
        s = set()
        for num in nums:
            if num > k and num not in s:
                s.add(num)
        return len(s)
