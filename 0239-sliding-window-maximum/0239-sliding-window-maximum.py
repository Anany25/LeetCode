class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        ans = []

        for i, num in enumerate(nums):
            while dq and dq[0] < i - k + 1:
                dq.popleft()

            while dq and nums[dq[-1]] < num:
                dq.pop()

            dq.append(i)

            if i >= k - 1:
                ans.append(nums[dq[0]])

        return ans
