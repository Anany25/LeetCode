from collections import defaultdict

class Solution:
    def countLargestGroup(self, n: int) -> int:
        digit_sum_counts = defaultdict(int)
        max_group_size = 0

        for num in range(1, n + 1):
            digit_sum = sum(map(int, str(num)))
            digit_sum_counts[digit_sum] += 1
            max_group_size = max(max_group_size, digit_sum_counts[digit_sum])

        return sum(1 for count in digit_sum_counts.values() if count == max_group_size)
