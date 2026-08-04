"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key= lambda x: x.end)
        prev_interval = None
        for interval in intervals:
            if prev_interval and prev_interval.end > interval.start:
                return False
            prev_interval = interval
        return True
