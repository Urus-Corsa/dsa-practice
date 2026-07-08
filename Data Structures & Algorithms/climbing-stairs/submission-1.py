class Solution:
    def climbStairs(self, n: int) -> int:
        """
        in this problem it looks like we have choices to make (1 step or 2 step at any ith position)
        Also it is possible to land on ith position multiple times from different paths
        this seems like has a recursive solution where we need to repeat making the same decisions from every step we land on recursive until we reach
        the top of the stairs (reach step n).
        brute force:
        starting at ground floor, we have 2 choices, either jump one step to 1 or jump two steps to 2. We first take on jump to 1, we havent reached step
        2 yet so we consider jumping one step or two steps. We try jumping one step and that lands us on step 2.
        So we go back to step 1, and jump two steps this time. We have gone onto step 3 (base case) so this jump path is invalid.
        And we return. We continuesly do this until done.
        So in brute force, if we consider our decision tree, we have two decisions to make and we roughly need to do this n times (height of this tree),
        so the time comp of this is O(2^n), and space comp is O(n) since our call stack only grow to size n.

        code:
        def climbStairs(n):
            def dfs(current_step):
                if current_step > n:
                    return 0 #invalid path
                if current_step == n:
                    return 1
                return dfs(current_step+1) + dfs(current_step+2)
            return dfs(0)

        optimized: memoization, top-down, caching, recursive
        So on each arbitary step, what info do I need to know the unique path from here to step n? If I know the number
        of unique ways to my current step[i].
        What decisions can I make? Decide to take 1 step or 2 steps at a time.
        Base case: once landed on n step (found a path), or once go past n step (was not a valid path)
        So if I could cache the unique ways that I could reach step n from ith step, then I can reduce my time comp
        to O(n) and the repeated calls in the tree can read directly from cache. Although the space is now O(n) + O(n) = O(2n)
        but in big O notation we know that gets reduced to just O(n) space.
        
        code:
        def climbStairs(n):
            cache = {}
            def dfs(current_step):
                if current_step == n:
                    return 1
                if current_step > n:
                    return 0
                if current_step in cache:
                    return cache[current_step]
                cache[current_step] = dfs(current_step+1)+dfs(current_step+2)
                return cache[current_step]
            return dfs(0)
        """
        cache = {}
        def dfs(current_step):
            if current_step == n:
                return 1
            if current_step > n:
                return 0
            if current_step in cache:
                return cache[current_step]
            cache[current_step] = dfs(current_step+1)+dfs(current_step+2)
            return cache[current_step]
        return dfs(0)