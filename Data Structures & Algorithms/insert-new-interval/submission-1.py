class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            #Case 1 if the new interval comes before 
            #the current interval
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]

            #Case 2 if the new interval comes after the current
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            
            #case 3: there is overlapping
            else:
                newInterval[0] = min(intervals[i][0], newInterval[0])
                newInterval[1] = max(intervals[i][1], newInterval[1])
        res.append(newInterval)
        return res