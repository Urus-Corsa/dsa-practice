class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        """
        from the problem statement it seems like that we need to use two pointers where one pointer iterates over the first list and the other iterates over the second while both allow for dynamic movement speed to be able to find intersections.
        
        with brute force approach we can pick one element from one list at a time and scan the other list for it to find the one that overlaps and then find intersection; 
        
        [0,2],[5,10],[13,23]
        [1,2],[8,12],[15,24]

        or one to be moving faster while the other moves slower.
        if end time of one is less than start time of the other, then no intersection.
        [0,5] merged, if overlap [max(start1, start2), min(finish1, finish2)] -> [1,2] appended to res, move the pointer of the interval that finishes sooner (firstList pointer moves), now compare [5,10] with [1,5] -> [5,5] appended to res, move pointer in secondList (it finishesh sooner) -> now compare [5,10] and [8,12] (overlap? yes, find intersection)->  [8,10] append to res, move pointer in firstList (finishes sooner) -> [13,23] and [8,12] overlap? no move the one who finishes sooner (secondList pointer moves) -> [13,23] and [15,24] overlap? yes-> [15,23] appended and so on
        Time comp needed for this, if len(firstList) = m and len(secondList) = n is O(m+n) to scan both, and space needed would be for res list is at most O(max(m,n)) where there is an intersection between all elements with both which at most can generate max(m,n) intersections
        """
        res = []
        if not firstList or not secondList:
            return res
        p1 = 0
        p2 = 0
        while p1 < len(firstList) and p2 < len(secondList):
            start1, end1 = firstList[p1]
            start2, end2 = secondList[p2]
            # do they overlap?
            if (end1 >= start2 and start1 <= start2) or (end2 >= start1 and start2 <= start1):
                res.append([max(start1,start2), min(end1,end2)])
            #else: they dont overlap
            if end1 > end2:
                p2 += 1
            elif end2 > end1:
                p1 += 1
            else:
                p1 += 1
                p2 += 1
        return res
        """
        dry tun:
        [0,2],[5,10]
        [1,2],[10,12]
        
        start1, end1 = 0,2
        start2, end2 = 1,2
        they overlap
        res.append([1,2])
        p1 += 1 -> p1 = 1
        p2 += 1 -> p2 = 1

        start1, end1 = 5,10
        start2, end2 = 10,12
        they overlap
        res.append([10,10])
        p1 += 1 -> p1 = 2
        p2 += 1 -> p2 = 2

        res = [[1,2],[10,10]] -> return
        """



