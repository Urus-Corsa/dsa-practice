class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        brute force is to generate all possible combination of coins where we can reach the target amount and return the min
        coins used from there. 
        we can utilize a backtracking approach where for each coin we have options to take every other coin including itself.
        We can do this until we reach the target amount, where we return min, or exceed it where hit base case and return.
        So for each coin, we have len(coins) = choices and we have to repeat this amount = m times. So height ot tree is O(amount)
        and we have n=len(coins) choices at each stage and we have to at most repeat it m times. So O(n^m) is the time comp to this backtracking
        solution.
        We also have to use recursion which takes up space in our memory for the size of the height of tree, so O(m) of space is needed

        [2,1] = 3

        recurse(0,0)
            in: recurse(0,2)
                in: recurse(0,4)
                    base case return 
                ex: recurse(1,2)
                    in: recurse(1,3)
                        found 1 return
                    ex: recurse(2,2)
                        base case OOB return
            ex: recurse(1,0):
                in: recurse(1,1)
                    in: recurse(1,2)
                        in: recurse(1,3)
                            found 1 return
                    ex: recurse(2,2)
                        base case OOB return
                ex: recurse(2,0)
                    base case OOB return        
                    
        we can see the overlapping subproblems, if at each stage we know the current coin that we can chose or not, and current amount occured
        we can make our decision for next state

        we can memoize our states as we go so repeat work becomes a cache hit instead of recursive call, this way our time comp becomes
        the time needed to search our space. O(n.m) and our space is O(n.m)
        """
        cache = {}
        def recurse(curr_i, curr_amount):
            if curr_amount == amount:
                return 0
            if curr_amount > amount or curr_i == len(coins):
                return -1
            if (curr_i, curr_amount) in cache:
                return cache[(curr_i, curr_amount)]
            skip = recurse(curr_i+1, curr_amount)
            pick = -1
            if curr_amount+coins[curr_i] <= amount:
                pick = recurse(curr_i, curr_amount+coins[curr_i])
            if pick != -1 and skip != -1:
                cache[(curr_i, curr_amount)] = min(pick+1, skip)
            elif pick == skip == -1:
                cache[(curr_i, curr_amount)] = -1
            elif pick != -1:
                cache[(curr_i, curr_amount)] = pick+1
            else:
                cache[(curr_i, curr_amount)] = skip
            return cache[(curr_i, curr_amount)]
        return recurse(0,0)
        