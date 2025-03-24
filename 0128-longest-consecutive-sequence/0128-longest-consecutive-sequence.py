class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        s = set()
        for num in nums:
            s.add(num)

        ans = 1
        for num in s:
            sub = 1
            if num-1 not in s:
                x = num + 1
                while x in s:
                    sub += 1
                    ans = max(sub, ans)
                    x += 1

        return ans