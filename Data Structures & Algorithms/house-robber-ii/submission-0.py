class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        we wanna maximize the taking values from non-adjacent elements from nums with a tiwst that the first house is adjacent to last.
        this means that if first house is robbed last house cannot be robbed, if first house is skipped, last house can be robbed.
        There are two ways we could go about this.
        We can define two dfs() functions where one stops after last house (considering first house), and other stops on last house (but 
        first house robbed). We could perform caching/memoization from the first dfs call where dfs(i) is going to be max we could rob starting
        from ith house to n, but actually this cache cannot be shared since the last house definitions in both dfs would be different. So this may
        not work and would be very inefficient. But we can try brute forcing it this way just to confirm that our idea works.
        So in brue force we will skipping caching for now to confirm idea of two dfs starting points. Oooh, aha!! I actually have an idea (lamp on moment!)
        How about if started from considering -1 position first (either rob and skip next, or skip and consider next), and then stop on n-1 house (consider it a base case
        since we started from there initially). This should work, as we will be able to comply with the circular constraint.
        So here if we did brute force, height of decision tree is still going to be n and since we have 2 decisions to make, our time comp will be
        O(2^n) and space would be O(n) for the growth of the recursion call stack.
        
        def rob(nums):
            n = len(nums)
            def dfs(current_house):
                if current_house >= n-1:
                    return 0 #we dont wanna consider last house (n-1) again as we have already in the begining
                return max(nums[current_house]+dfs(current_house+2), dfs(current_house+1))
            return dfs(-1)
        
        If we used memoization for each state and cached each recursive call that returns, we would know from each position and onwards what would be the
        max we can rob so we can just have a cache hit and reduce the time to O(n) instead with a bit trade in space of O(n) for cache as well as O(n)
        for recursion call stack. So space would be O(2n) which simplifies to O(n)

        def rob(nums):
            n = len(nums)
            cache = {}
            def dfs(current_house):
                if current_house >= n-1:
                    return 0
                if current_house in cache:
                    return cache[current_house]
                return max(nums[current_house]+dfs(current_house+2), dfs(current_house+1))
            return dfs(-1)
        """
        n = len(nums)
        cache = {}
        def dfs(current_house, robbed_first):
            if current_house >= n:
                return 0
            if current_house == n-1:
                if robbed_first:
                    return 0
            if (current_house, robbed_first) in cache:
                return cache[(current_house, robbed_first)]
            if current_house != 0:
                cache[(current_house, robbed_first)] =  max(nums[current_house]+dfs(current_house+2, robbed_first), dfs(current_house+1, robbed_first))
            else:
                cache[(current_house, robbed_first)] =  max(nums[current_house]+dfs(current_house+2, True), dfs(current_house+1, False))
            return cache[(current_house, robbed_first)]
        return dfs(0, False)