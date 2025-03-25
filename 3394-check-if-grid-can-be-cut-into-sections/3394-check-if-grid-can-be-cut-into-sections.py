class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:

        x_intervals, y_intervals = [], []
        for sX, sY, eX, eY in rectangles:
            x_intervals.append([sX, eX])
            y_intervals.append([sY, eY])

        x_intervals.sort()
        lines =  0
        head, last = x_intervals[0][0], x_intervals[0][1]
        for line in x_intervals[1:]:
            start, end = line
            if start >= last:
                lines += 1
                head = start
                last = end
            else:
                last = max(last,end)
            if lines ==2:
                return True

        y_intervals.sort()
        lines =  0
        head, last = y_intervals[0][0], y_intervals[0][1]
        for line in y_intervals[1:]:
            start, end = line
            if start >= last:
                lines += 1
                head = start
                last = end
            else:
                last = max(last,end)
            if lines ==2:
                return True


        return False
    
