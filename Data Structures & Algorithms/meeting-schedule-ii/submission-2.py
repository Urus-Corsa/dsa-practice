"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        """
        (5,10),(10,20),(1,25)

        =[(1,3),(4,6),(2,26),(3,37),(4,38),(2,9)]
        """
        if not intervals:
            return 0
        intervals.sort(key=lambda x:x.start)
        rooms_count = 1
        soonest_exisiting_room_gets_available = []
        heapq.heappush(soonest_exisiting_room_gets_available, intervals[0].end)
        for i in range(1, len(intervals)):
            next_start, next_end = intervals[i].start, intervals[i].end
            if next_start<soonest_exisiting_room_gets_available[0]:
                heapq.heappush(soonest_exisiting_room_gets_available, next_end)
                rooms_count += 1
            else:
                heapq.heappushpop(soonest_exisiting_room_gets_available, next_end)
        return rooms_count