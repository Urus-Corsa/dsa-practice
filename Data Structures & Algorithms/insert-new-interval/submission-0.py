class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        brute force: append newInterval to the end of intervals and sort and then begin with merging overlappig intervals.
        If intervals has len of n, it'd take O(nlogn) to sort + O(n) to do a linear scan for merging and then return. So time would be O(nlogn)
        Space needed would be O(n) for merged intervals to be inserted.

        Optimized: rather than append, sort, merge we can just start inserting the non-overlapping intervals in intervals until we reach the first overlapping interval. Once there, we merge and insert and for the rest we merge and insert. This would take O(n) as there won't be a need to sort again, and would still need O(n) space for the new interval to be inserted.
       
       [0,1],[2,4],[9,11]
       [1,6]
       """
        updated_intervals = []
        i = 0
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            updated_intervals.append(intervals[i])
            i += 1
    
        updated_intervals.append(newInterval)    

        while i < len(intervals):
            start, end = intervals[i]
            prev_start, prev_end = updated_intervals[-1]
            if start > prev_end:
                updated_intervals.append(intervals[i])
            else:
                updated_intervals[-1][0] = min(prev_start, start)
                updated_intervals[-1][1] = max(prev_end, end)
            i += 1
        return updated_intervals