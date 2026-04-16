"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)
        for i in range(1, len(intervals)):
            this_meeting_end = intervals[i-1].end
            next_meeting_start = intervals[i].start
            if this_meeting_end>next_meeting_start:
                return False
        return True