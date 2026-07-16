"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) == 0:
            return 0
        if len(intervals)==1:
            return 1
        
        res, count = 0, 0

        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        sp, ep = 0, 0

        while sp < len(intervals):
            if start[sp] < end[ep]:
                sp += 1
                count += 1
            else:
                ep += 1
                count -= 1
            
            res = max(res, count)
        
        return res


        