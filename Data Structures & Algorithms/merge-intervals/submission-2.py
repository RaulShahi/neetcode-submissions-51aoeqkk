class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals=sorted(intervals, key=lambda x:x[0])
        print(intervals)
        ans = [intervals[0]]

        for i in range(1, len(intervals)):
            high = intervals[i][1]
            low = ans[-1][0]
            mid1 = ans[-1][1]
            mid2 = intervals[i][0]

            if mid1 >= mid2:
                #merging required
                low = min(low, mid2)
                high = max(mid1, high)
                ans[-1] = [low, high]
            
            else:
                #push to ans
                ans.append(intervals[i])        
        return ans
