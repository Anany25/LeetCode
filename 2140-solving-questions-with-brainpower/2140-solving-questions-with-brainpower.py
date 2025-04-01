class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:

        n = len(questions)
        res = [0] * (n + 1)  # res[i] = max points from question i to end

        for i in range(n - 1, -1, -1):
            point, skip = questions[i]
            next_q = i + skip + 1
            solve = point + (res[next_q] if next_q < n else 0)
            skip = res[i + 1]
            res[i] = max(solve, skip)

        return res[0]
