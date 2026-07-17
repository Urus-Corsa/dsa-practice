class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        cache = {}
        def recurse(item_index, w):
            if item_index >= len(profit) or w > capacity:
                return 0
            if (item_index, w) in cache:
                return cache[(item_index, w)]
            take = 0
            if w+weight[item_index] <= capacity:
                take = profit[item_index]+recurse(item_index+1, w+weight[item_index])
            not_take = recurse(item_index+1, w)
            cache[(item_index, w)] =  max(take,not_take)
            return cache[(item_index, w)]
        return recurse(0,0)
