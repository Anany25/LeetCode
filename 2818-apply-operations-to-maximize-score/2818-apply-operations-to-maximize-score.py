import heapq
from typing import List

class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        # 1. Precompute prime scores using sieve
        prime_scores = [0] * (10**5 + 1)
        for i in range(2, 10**5 + 1):
            if prime_scores[i] == 0:
                for j in range(i, 10**5 + 1, i):
                    prime_scores[j] += 1

        # 2. Monotonic stack to get left and right bounds
        left = [-1] * n
        right = [n] * n
        stack = []

        # Strictly less for left
        for i in range(n):
            while stack and (prime_scores[nums[stack[-1]]] < prime_scores[nums[i]]):
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)

        stack.clear()

        # Strictly less for right
        for i in range(n - 1, -1, -1):
            while stack and (prime_scores[nums[stack[-1]]] <= prime_scores[nums[i]]):
                stack.pop()
            right[i] = stack[-1] if stack else n
            stack.append(i)

        # 3. Use max heap (simulate max with -val)
        heap = []
        for i in range(n):
            freq = (i - left[i]) * (right[i] - i)
            heapq.heappush(heap, (-nums[i], freq))

        # 4. Greedy multiplication
        score = 1
        while k > 0 and heap:
            val, freq = heapq.heappop(heap)
            val = -val
            use = min(freq, k)
            score = score * pow(val, use, MOD) % MOD
            k -= use

        return score
