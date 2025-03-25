class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        
        x_intervals = [[rectangles[i][0], rectangles[i][2]] for i in range(len(rectangles))]
        y_intervals = [[rectangles[i][1], rectangles[i][3]] for i in range(len(rectangles))]

        x_intervals.sort()
        y_intervals.sort()

        def helper(intervals):
            lines =  0
            head, last = intervals[0][0], intervals[0][1]
            for line in intervals[1:]:
                start, end = line
                if start >= last:
                    lines += 1
                    head = start
                    last = end
                else:
                    last = max(last,end)
            return lines >=2

        return helper(x_intervals) or helper(y_intervals) 