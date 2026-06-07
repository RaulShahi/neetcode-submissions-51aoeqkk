class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        ans = [intervals[0]]

        for i in range(1, len(intervals)):
            cur_start, cur_end = intervals[i]
            last_start, last_end = ans[-1]

            if last_end >= cur_start:
                #merging required => which is the greater element between the ends
                #sorting guarantees that the first element of ans is less than of intervals[i]
                ans[-1][1] = max(last_end, cur_end)
            else:
                ans.append(intervals[i])
        
        return ans
        