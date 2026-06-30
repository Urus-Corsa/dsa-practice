class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        nums = [2,12,2,3,0,1,-1], k=2
        if n is the len of nums:
        {2:2,12:1,3:1,0:1,-1:1}, O(n^2) naively compare each element of time, O(n) space for freq dict
        [(2,2),(1:12),(1:3),(1:0),(1:-1)] O(n) to write tuples, and o(nlogn) to sort based on frequency
        [2,1] from the sorted array after k iterations. O(k) of time and O(k) of space for res array.

        improved:
        THIS IS IMPORTANT:
        n = len(nums)
        u = len(set(nums)) #number of unqiue elems in nums a.k.a keys in freq dict
        k = number of most freq elems
        traverse and populate freq dict:
        dont need nested loop to get counts, use dict, if elem is there then increment its count if not add it with 1 as default
        this will save us a factor of O(n) to fill in the dict, so the time to fill in freq dict becomes O(n) and the size it will
        grow to will become maximum of O(u), so time O(n) and space O(u) so far.

        to sort, there is a trade off here based on how the input is received, but due to given constraint:
        
        1. max heap approach: in order to use a heap, we need to extract the keys and freq into list of tuples with 
        (-freq (negative sign cauz max heap), unique elem) which will take us O(u) time to extract and O(u) space 
        to write to list.

        Then we RUN 
        HEAPIFY it will sort it with O(u) time a.k.a total number of unique elems inside (no extra space needed, same arr is now a heap).
        **NOTE** if just do heappush here instead of heapify it will take O(ulogu) to do a push CUZ size grows to U, while each push requires heap to 
        pefrom sorting u elemes which is logu op, and we do this for all u elems, and it will take O(ulogu) times for heappush rather than O(u) for heapify.
        
        Then We need to pop from this heap of size u, k times into res list, so it will take O(klogu) time to pop, and O(k) space to generate res list of size k.

        So using max heap, total time will be
        1. traverse nums: O(n) + extract dict items into list O(u) + heapify on list O(u) + pop k times from max heap O(klogu)
        Total time: O(n+u+u+klogu) which would be ~ O(n+u+klogu), in the worst case where u == n (u <= n always), time is
        O(3n+klogn) ~ O(n+klogn), if k in the worst case k == n (k <= n always, but note that if k is as large as n then all elements are unique for sure
        because of this constraint 1 <= k <= number of distinct elements in nums. So if k == n, then also u == n but vice versa of this is not true if u == n,
        k is not necessaily k != n), this becomes O(n+nlogn) where O(nlogn) dominates
        in simplified term.



        2. min heap approach (better than max heap):
        To use a min heap, we can't just create list with (freq, unqiue elem) and call heapify on it because it will have all lowest freq elems sorted to be popped first.
        Then we will have to do pops to reach the size of K where we know what's in there is already the k remaining highest freq elems.
        INSTEAD, we try to keep our heap at most of size k. So here we do heap push INSTEAD of heapify, where will push at most u items into min heap that will always 
        maintain its size of k. The time to do this will be O(ulogk), and space for heap will be O(k). Here if k ever becomes n, we again have O(nlogn) as well.

        OPTIMAL SOLUTION TO THIS (NOT HEAP)
        1. traverse, fill in freq dict. 
        2. use a bucket/ a list of size n with indecies being the maximum freq an elem can have (if all elems in num is same, max freq is n), so we create list of size
        n and then traverse the dict items, for each index we add those elems that have freq == index into a list at that index (this is a 2D arr, each elem
        here represents list of all elems in nums that have freq index). Then we go the end of this list (highest index aka highest freq), and add k elems to res and return.

        Time: O(n) traverse nums + O(n) create bucket and assign empty initial list to each index + O(u) to fill in bucket with unique elems + O(k) to populate res
        Time total: O(n+n+u+k), here the worst case where k == n and u == n would become O(4n) and that gets simplified to O(n) in big O
        Space: O(u) freq dict + O(n+u) bucket of size n where one index can have all elems (u == n) + O(k) for output if we count it.
        Space Total: O(u+n+u+k) in worst case k == n and u == n so O(4n) ~ O(n)
        """
        freq = defaultdict(int)
        res = []
        bucket = [[] for i in range(len(nums)+1)]

        for n in nums:
            freq[n] += 1
        for n, count in freq.items():
            bucket[count].append(n)
        for i in range(len(bucket)-1, 0, -1):
            this_bucket = bucket[i]
            for j in range(len(this_bucket)):
                res.append(this_bucket[j])
                if len(res) == k:
                    return res
