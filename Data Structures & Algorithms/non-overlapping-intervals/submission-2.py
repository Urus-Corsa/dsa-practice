class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        sweep line algorithm would work here. We can assign each interval start time a 1 and each end time a -1 and we can sum up the scores and the max reached indicates that tere are that number of overlapping intervals.
        """
        intervals.sort(key = lambda x: x[0])
        print(intervals)
        prev = intervals[0]
        overlap_count = 0
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            prev_start, prev_end = prev
            if start >= prev_end: # no overlaps
                prev = intervals[i]
                continue
            # overlaps
            overlap_count += 1
            prev = [prev_start, min(prev_end, end)]
        return overlap_count

        # timeline = []
        # for interval in intervals:
        #     start, end = interval
        #     timeline.append((start, 1))
        #     timeline.append((end, -1))
        # timeline.sort(key = lambda x: (x[0],x[1]))
        # print(timeline)
        # curr_overlaps = 0
        # max_overlaps = 0
        # for time in timeline:
        #     score = time[1]
        #     curr_overlaps += score
        #     max_overlaps = max(max_overlaps, curr_overlaps)
        # return max_overlaps