class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        s = set(nums)
        ans = 0
        for num in s:
            if num-1 not in s:
                sub = 1
                x = num + 1
                while x in s:
                    sub += 1
                    x += 1
                ans = max(sub, ans)

        return ans