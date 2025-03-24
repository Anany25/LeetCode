class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        print(meetings)
        last = meetings[0][0]
        ans = 0 + last - 1
        for meet in meetings:
            i = meet[0]
            j = meet[1]
            print(i,last)
            if i > last:
                ans += i - last - 1
            last = max(j,last)

        return ans + (days -last)