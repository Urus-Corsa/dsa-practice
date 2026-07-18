class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
        in this problem, we have an array where we need to find two subsets of (each subset includes
        a combination of elements from the original array in it where the order of the elements can be
        shuffled however the elements in each subset cannot be repeated). 
        Ideas that come to mind: Know total sum, and see whether you can pick two subsets.
        
        [3,1,2,1], find two subsets with same sum.
        total sum = 7
        sorted = [1,1,2,3]
        prefix sum = p=1, t=6 | p=2, t=5 | p=4, t=3 at this point since we know that array is sorted
        and have already bypassed the half sum that we were looking for, we know we can't reach a point
        where sums are equal. Also, with this we are not considering subsets, subset could be any non repeating
        combinations of the elements in array.

        So since our greedy approach doesnt work, let's look at brute force and then we can see how 
        we can optimize the solution.
        So in order to generate all subsests, we basically need to consider all combinations for each element
        with other elements.
        for i in range(len(nums)):
            subarr = [i]
            for j in range(len(nums)):
                
                for k in range(len(nums)):
                if i == j:
                    continue
                sub_arr.append(nums[j])
        """
        total_sum = sum(nums)
        if total_sum%2 != 0:
            return False
        target_sum = total_sum//2
        cache = {}
        def recurse(curr_i, curr_sum):
            if curr_sum == target_sum:
                return True
            if curr_sum > target_sum or curr_i >= len(nums):
                return False
            if (curr_i, curr_sum) in cache:
                return cache[(curr_i, curr_sum)]
            include = recurse(curr_i+1, curr_sum+nums[curr_i])
            #if either include or not include return true, return true
            not_include = False
            if include == False:
                not_include = recurse(curr_i+1, curr_sum)
            cache[(curr_i, curr_sum)] = True if include or not_include else False
            return cache[(curr_i, curr_sum)]
        return recurse(0,0)