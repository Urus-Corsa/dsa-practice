class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        cache = {}
        def recurse(curr_i, curr_w):
            if curr_i == len(profit):
                return 0
            if (curr_i, curr_w) in cache:
                return cache[(curr_i, curr_w)]
            exclude = recurse(curr_i+1, curr_w)
            include = 0
            if curr_w + weight[curr_i] <= capacity:
                include = profit[curr_i] + recurse(curr_i, curr_w + weight[curr_i])
            cache[(curr_i, curr_w)] = max(include, exclude)
            return cache[(curr_i, curr_w)]
        return recurse(0,0)