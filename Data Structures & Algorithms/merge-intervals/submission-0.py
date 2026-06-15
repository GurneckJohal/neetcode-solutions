class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1: return intervals

        intervals.sort()

        res = []
        candidate = intervals[0]
        for i in range(1, len(intervals)):
            if candidate[1] >= intervals[i][0]:
                candidate[1] = max(intervals[i][1], candidate[1])
            else:
                res.append(candidate)
                candidate = intervals[i]
        
        res.append(candidate)

        return res
