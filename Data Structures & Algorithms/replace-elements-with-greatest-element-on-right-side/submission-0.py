class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        """
        brute force: O(n^2), for each element scan all elems to its right to find max and right to res
        if res counts, space is O(n) if it doesn't O(1)

        Optimal, if we started from last position until the first, the max is what's on the right until there is a new max
        one pass in reverse. O(n)
        """
        res = [0 for i in range(len(arr))]
        res[len(arr)-1] = -1
        max_seen = arr[-1]
        for i in range(len(arr)-2, -1, -1):
            max_seen = max(max_seen, arr[i+1])
            res[i] = max_seen
        return res