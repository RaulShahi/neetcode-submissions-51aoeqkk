"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

from heapq import *
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        
        heap = []

        intervals.sort(key = lambda x:x.start)
        print(intervals)

        for interval in intervals:
            if(heap and heap[0] <= interval.start):
                #if the earliest end time(heap[0]) is less than the start tiem
                #one meeting has already ended, so another once can be started
                heappop(heap)
            
            heappush(heap, interval.end)
        
        return len(heap)
        