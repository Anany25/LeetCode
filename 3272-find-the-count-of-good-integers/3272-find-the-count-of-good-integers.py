from math import factorial
from collections import Counter

class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        
        fact = [1] * (n + 1)
        for i in range(2, n + 1):
            fact[i] = fact[i - 1] * i
        
        def gen_palindrome(n):
            half = (n + 1) // 2
            start = 10 ** (half - 1)
            end = 10 ** half

            for first_half in range(start, end):
                s = str(first_half)
                full = s + s[-2::-1] if n % 2 else s + s[::-1]
                yield int(full)

        def count_permutations(counter, n):
            total = fact[n]
            for c in counter.values():
                total //= fact[c]

            if '0' in counter:
                if counter['0'] == n:
                    return 0
                counter['0'] -= 1
                sub_total = fact[n - 1]
                for c in counter.values():
                    sub_total //= fact[c]
                counter['0'] += 1
                total -= sub_total
            return total

        seen = set()
        total = 0
        for p in gen_palindrome(n):
            if p % k != 0:
                continue
            digits = tuple(sorted(Counter(str(p)).items()))
            if digits in seen:
                continue
            seen.add(digits)
            counter = Counter(dict(digits))
            total += count_permutations(counter, n)
        return total
