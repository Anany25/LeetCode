class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        s = defaultdict(int)
        for i in nums:
            s[i] += 1

        maxi = max(s, key=s.get)
        
        count = 0
        n = len(nums)

        for i in range(n):
            if nums[i] == maxi:
                count += 1
            if count > (i + 1) / 2 and s[maxi] - count > (n - i - 1)/ 2:
                return i

        return -1 


