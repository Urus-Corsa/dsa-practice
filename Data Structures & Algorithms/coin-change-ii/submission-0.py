class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache = {}
        def recurse(curr_i, curr_amount):
            if curr_amount == amount:
                return 1
            if curr_i >= len(coins) or curr_amount > amount:
                return 0
            if (curr_i, curr_amount) in cache:
                return cache[(curr_i, curr_amount)]
            skip = recurse(curr_i+1,curr_amount)
            take = 0
            if curr_amount+coins[curr_i] <= amount:
                take = recurse(curr_i, curr_amount+coins[curr_i])
            cache[(curr_i, curr_amount)] = take+skip
            return cache[(curr_i, curr_amount)]
        return recurse(0,0)