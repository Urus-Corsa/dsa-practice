class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        b.f: for each element, count the occurances (O(n^2)) and append them with as a tuple to an freq array, and add the counted
        elem to a set to not count again. then once done, sort the freq array (O(nlogn)) on the frequency of each elem, and for k iterate
        over freq array and append the elements of the highest freqs from their tuples to the res arr and return
        Time for this would be O(n^2 + nlogn + n) which O(n^2) dominates here
        Space for this would be O(n) for freq array.

        improved: use a dict instead of counting each occurance with a nested loop (o(n)), and then turn the values of the
        dict and keys into tuples O(n), add them to an arr and sort in descending order O(nlogn), and return top k O(k).
        Time would be O(n + n + nlogn) ~ O(nlogn) dominates here
        Space would be O(n+n) ~ O(n) (one for the dict one for the arr)

        optimized:
        We can start by counting freq of each num and storing them in dict (O(n)). Then we can use an approach where it's
        similar to bucket sort that we initialize an arr as large as n+1 that each of its indecies indicates the number of times
        elements have appeared. So if n is 5, then we initialize an arr of size 6 (n+1 because we need indecies 1-5 to correspond to freq of nums)
        and then we go through the values of the dict and add their keys to the corresponding index and then return the top k elements
        """
        freq = defaultdict(int)
        occurances = [[] for i in range(len(nums)+1)]
        for n in nums:
            freq[n] += 1
        for n, count in freq.items():
            occurances[count].append(n)
        res = []
        for i in range(len(occurances)-1,0,-1):
            for j in range(len(occurances[i])):
                res.append(occurances[i][j])
                if len(res) == k:
                    return res