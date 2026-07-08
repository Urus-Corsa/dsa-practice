class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        this problem is asking us to get max money we can rob from houses which their values are in nums without setting off the alarm.
        It also tells us for each house we rob, we must have not had the previous house robbed nor can we rob the next house. So we basically
        have 2 options/decisions to make. At each house we can either rob it or not rob it. Here our decisions have consequences. If we 
        robbed this house, we cant land on next/adjacent house because we will set off the alarm. So if we robbed ith house, we need
        to land on i+2 house to decide again. Other option is that we don't rob ith house that we are looking at right now and we 
        get to land on next adjacent house and make these decisions there again.
        Since each decision that we make has an impact to the decisions that we are gonna make in the future, and we are repeatedly and 
        recursively going to make the same decision each time. Notice that at each recursive call we are trying to know what's the max
        we can rob if we started from this ith/arbitary house (we don't necessairly have to rob the ith house since max could be calculated by not
        robbing the current and getting ability to run i+1 house). 
        So the state, dfs(i) = max money that can be robbed from the remaining houses if we considered i as our starting position.
        decisions:rob current and jump to two houses or skip current and rob next.
        So recurrence is dfs(i) = max(nums[i]+dfs(i+2), dfs(i+1))
        base case is that we have reached out of bounds (no more house), we just return 0 since there is nothing else to rob

        Here is decision tree, we have 2 decisions to make, one is to rob current and skip next and the other is to skip current and rob next.
        We need to repeat this decision for every house we land on. This means decision tree could grow as deep as number of houses in nums == len(nums)
        So, O(2^n) is time comp for this recursive b.f solution, and O(n) for space since recurssion call stack can only grow as large as number
        of houses and then we hit base case and return.

        Code:
        def rob(nums):
            n = len(nums)
            def dfs(i):
                if i >= n:
                    return 0 #no more houses
                return max(nums[i]+dfs(i+2), dfs(i+1))
            return dfs(0)

        Optimized, top-down, recursive approach
        we can cache dfs(i)/answer to subproblem i once calculated so if through other paths we arrived at ith house that we have already processed
        its max that can be robbed in total from this position onwards. We can reduce our time comp to O(n) and time would be O(2n)~O(n) because of cache + 
        recursion call stack
        """
        n = len(nums)
        cache = {}
        def dfs(i):
            if i >= n:
                return 0
            if i in cache:
                return cache[i]
            cache[i] = max(nums[i]+dfs(i+2), dfs(i+1))
            return cache[i]
        return dfs(0)