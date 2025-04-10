class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        b, f = str(start - 1), str(finish)
        def helper(s1, s2, limit):
            d = len(s1) - len(s2)
            if d < 0:
                return 0
            elif d == 0:
                return 0 if s2 > s1 else 1
            suf = s1[d:]
            cnt = 0
            for i in range(d):
                if limit < int(s1[i]):
                    cnt += (limit + 1) ** (d - i)
                    return cnt
                cnt += int(s1[i]) * (limit + 1) ** (d - i - 1)
            if suf >= s2:
                cnt += 1
            return cnt
        return helper(f, s, limit) - helper(b, s, limit)