def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    if len(intervals) < 1:
        return intervals
    intervals = sorted(intervals, key=lambda intervals: intervals[0])
    l = [[]]
    maxi = len(intervals) - 1
    i = 0
    while i <= maxi:
        if i < maxi and intervals[i][1] >= intervals[i+1][0] and intervals[i+1][1] >= intervals[i][1]:
            intervals[i+1][0] = intervals[i][0]
            intervals.pop(i)
            maxi -= 1
            continue
        if i < maxi and intervals[i][1] >= intervals[i+1][0] and intervals[i+1][1] <= intervals[i][1]:
            intervals.pop(i+1)
            maxi -= 1
            continue
        i += 1
    return intervals
