class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        n = len(nums)
        nums_set = set(nums)   # O(n) to build the set
        for i in range(1, n + 1):
            if i not in nums_set:  # O(1) on average
                return i
        return n + 1
