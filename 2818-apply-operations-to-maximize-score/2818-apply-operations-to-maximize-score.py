from typing import List
import math

class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        n = len(nums)


        def prime_score(x):
            score = 0
            for p in range(2, int(math.sqrt(x)) + 1):
                if x % p == 0:
                    score += 1
                    while x % p == 0:
                        x //= p
            if x > 1:
                score += 1
            return score

        s = [prime_score(num) for num in nums]

        left = [-1] * n
        right = [n] * n
        stack = []

        for i in range(n):
            while stack and s[stack[-1]] < s[i]:
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)

        stack.clear()

        for i in range(n - 1, -1, -1):
            while stack and s[stack[-1]] <= s[i]:
                stack.pop()
            right[i] = stack[-1] if stack else n
            stack.append(i)

        ranges = [(nums[i], (i - left[i]) * (right[i] - i), i) for i in range(n)]


        ranges.sort(reverse=True)

        result = 1
        for val, freq, i in ranges:
            take = min(freq, k)
            result = result * pow(val, take, MOD) % MOD
            k -= take
            if k == 0:
                break

        return result
