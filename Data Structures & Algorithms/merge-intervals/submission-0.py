class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        sort intervals by start time, this allows for intervals to be sorted by their start time meaning that each interval would either start entirely after its previous, or overlap and (1. be obsorbed; meaning its end time is less than or equal to previous' end time, or be merged; meaning its start time is before or equal previous' end)

        if intervals list has len of n, sorting would take O(nlogn) and the linear scan would take O(n). Space needed would be for all intervals to be merged and written to a new list. This means that the res list would at most have size of n so space is bounded by O(n)
        """
        intervals.sort(key= lambda x: x[0])
        merged = [intervals[0]]
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            merged_start, merged_end = merged[-1]
            if start > merged_end: #non-overlapping
                merged.append(intervals[i])
                continue
            merged[-1][1] = max(merged_end, end)
        return merged