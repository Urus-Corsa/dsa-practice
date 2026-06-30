class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        think b.f, O(n^2) BECAUSE it has to consider each element be start of a sequence and check the rest in nums
        BUT
        we only need to count from begining of each sequence, not count from every element. If we convert nums to set
        to check if num-1 in nums set, if it is then this num is not the beginig of a sequence, we will count this sequence once we reach
        the begining of its sequence where num-1 is not in nums.
        For each begining of sequence, we count increments until the sequence breaks and we take note of max seen, at the end return
        """
        nums_set = set(nums)
        longest_seq_count= 0
        for n in nums:
            if n-1 in nums_set:
                continue
            num = n
            this_seq_count = 0
            while num in nums_set:
                this_seq_count += 1
                num += 1
            longest_seq_count = max(longest_seq_count, this_seq_count)
        return longest_seq_count