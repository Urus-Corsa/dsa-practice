import heapq
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
        sort by finish time
        first interval takes a room, from second interval and onwards, we check if the interval overlaps with the interval that is up to finish first. If it does then new room, if it doesnt then put it in that same room and update the time to the next meeting in a room finishing next (a heap can help pop whatever meeting is "assigned to a room currently" or was processed last for that room).
        intervals = [(0,40),(5,10),(15,20)] -> [(5,10),(15,20),(0,40)] -> room assigned to (5,10), next meeting starts after it, so we give it the same room, pop that meeting and push (15,20), now next one comes in (0,40) and it overlaps so we assign new room, and push into the heap. 
        intervals = [(1,4),(2,4),(2,3),(0,3),(1,5)] -> [(0,3),(2,3),(1,4),(2,4),(1,5)] this won't work

        Sweep line algo: Just leanred! Goal is to see how many overlapping event we have (notice how we are considering the intervals to be events now that have a start and finish time.) Sort by start time, for each new event that starts we increment and when one finishes we decrement current count and at the end we return global max that we saw. We are essentially converting the intervals onto a linear (where line comes from in the name) timeline that we are gonna mark each start and finish time of the events. The time period that holds the most amount of counts of active events that will be our max overlaps.
        
        implementation:
        sort by start time
        then use a heap for finish times. insert the first interval in, while the start of the intervals hasn't reached the peak of heap's end time we increment, and when we reach a time where the next start time is greater than the peak of the heap finish time, then we pop, we do the same comparison again until we are done processing all intervals. In this implementation the max size that the heap ever grows to it'd be max number of overlapping intervals/events

        Time: If n is the size of the intervals input list then O(nlogn) to sort, and linear scan of the line O(n) and for each push onto the heap and pop we are looking at logn time and since we will at most push and pop all intervals at most once this would be O(nlogn) as well. Total time comp would be O(2*(nlogn) + n) which simplifies to O(nlogn)

        Space: we need space for the heap which will grow to at most size of n (in the case where all intervals are inserted without getting popped), so O(n) space comp.
        """
        if not intervals:
            return 0
        intervals.sort(key=lambda x:x.start)
        heap = []
        heapq.heappush(heap, intervals[0].end)
        rooms_needed = 1
        for i in range(1, len(intervals)):
            if intervals[i].start >= heap[0]:
                heapq.heappop(heap)
            heapq.heappush(heap, intervals[i].end)
            rooms_needed = max(rooms_needed, len(heap))
        return rooms_needed