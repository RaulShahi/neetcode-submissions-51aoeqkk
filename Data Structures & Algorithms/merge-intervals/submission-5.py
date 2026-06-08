class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        ans = [intervals[0]]

        for i in range(1, len(intervals)):
            cur_start, cur_end = intervals[i]
            prev_start, prev_end = ans[-1]

            if prev_end >= cur_start:
                #merging required
                ans[-1] = [prev_start, max(cur_end, prev_end)]
            else:
                ans.append(intervals[i])
        
        return ans
        