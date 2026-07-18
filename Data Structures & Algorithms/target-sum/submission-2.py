class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        nums_sum = sum(nums)
        if nums_sum == 0 and target == 0:
            return 2**(len(nums))
        cache = {}
        def recurse(curr_i, curr_sum):
            if curr_i == len(nums) and curr_sum == target:
                return 1
            if curr_i >= len(nums):
                return 0
            if (curr_i, curr_sum) in cache:
                return cache[(curr_i, curr_sum)]
            add = recurse(curr_i+1, curr_sum+nums[curr_i])
            subtract = recurse(curr_i+1, curr_sum-nums[curr_i])
            cache[(curr_i, curr_sum)] = add+subtract
            return cache[(curr_i, curr_sum)]
        return recurse(0,0)
