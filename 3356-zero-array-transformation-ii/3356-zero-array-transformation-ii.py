class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        
        n = len(nums)
        cum = [0] * (n)


        zero = True
        for i in nums:
            if i > 0:
                zero = False

        if zero is True:
            return 0

        for x in queries:
            cum[x[0]] += x[2]

            if x[1] + 1 < n:
                cum[x[1] + 1] -= x[2]

        cur = 0

        for i in range(n):
            cur += cum[i]
            if cur < nums[i]:
                return -1
        
        cum = [0] * (n)

        for k, x in enumerate(queries):
            cum[x[0]] += x[2]

            if x[1] + 1 < n:
                cum[x[1] + 1] -= x[2]

            cur = 0
            flag = True
            for i in range(n):
                cur += cum[i]
                if cur < nums[i]:
                    flag = False
                    break
            
            if flag:
                return k+1
