class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[0])
        ans = 0

        print(intervals)
        prevEnd = intervals[0][1]
        for i in range(1, len(intervals)):
            cur_start, cur_end = intervals[i]
            

            if cur_start >= prevEnd:
                prevEnd = cur_end
            else:
                ans += 1
                prevEnd = min(prevEnd, cur_end)
        return ans