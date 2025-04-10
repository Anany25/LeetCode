class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        @cache
        def fn(val: str, i: int, is_smaller: bool) -> int:
            if len(val) < len(s): return 0
            if len(val) == len(s): return val >= s
            if i == len(val) - len(s): return not is_smaller or val[i:] >= s
            ans = 0
            if is_smaller and int(val[i]) <= limit:
                ans += (int(val[i])) * fn(val, i + 1, False)
                ans += fn(val, i + 1, True)
            else: ans += (1 + limit) * fn(val, i + 1, False)
            return ans
        
        return fn(str(finish), 0, True) - fn(str(start - 1), 0, True)