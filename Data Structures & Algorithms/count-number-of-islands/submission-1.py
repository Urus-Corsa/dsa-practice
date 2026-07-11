class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        In this prob we basically need to perform a discovery traversal from every "1" cell that we encounter while traversing the grid
        and move to the 4-adj land cells that we are allowed to move to while accounting for it being part of the same island. Then once the island is finished
        we move on to the rest of our traversal of the grid and begin our discovery search from the next 1 cell that we encounter as long as we 
        have not visited as part of an already discovered island before. We continue with this until we finish the full traversal of the grid.
        In other words we are going to begin traversing the grid from the top left corner to the bottom right corner, and durig traversal for every cell that its 
        value is 1 and we have not marked it as seen before, we start a dfs to discover all the islands connected to it. For every dfs we start we 
        increment our island counter, and once we reach the bottom right corner we can return the counter.
        if the number of rows in the grid is m and size of each row is n, the time comp to perform a full traversal will be O(m.n), now during this traversal
        that we start a dfs, in the worst case, one traversal could take O(m.n) as well (all cells are lands). So time would be O((m.n)^2), and the space
        needed for this will be to maintain a set of visited cells which could grow as large as O(m.n) (all cells are lands) and the recursion call stack
        size which could also grow as large as O(m.n) (all cells are lands), so space would be O(2(m.n))~O(m.n)
        """
        if not grid:
            return 0
        m = len(grid) #rows
        n = len(grid[0]) #cols
        dirs = [(1,0),(0,1),(-1,0),(0,-1)]	
        count = 0

        def dfs(r, c):
            if not (0 <= r < m and 0 <= c < n) or grid[r][c] != "1":
                return
            grid[r][c] = "0"
            for dr, dc in dirs:
                nr, nc = dr+r, dc+c
                dfs(nr,nc)

        def bfs(r,c):
            q = deque()
            q.append((r,c))
            grid[r][c] = "0"
            while q:
                row, col = q.popleft()
                for dr, dc in dirs:
                    nr, nc = dr+row, dc+col
                    if 0<=nr<m and 0<=nc<n and grid[nr][nc] == "1":
                        grid[nr][nc] = "0"
                        q.append((nr,nc))
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    count += 1
                    # dfs(i,j)
                    bfs(i,j) 
        
        return count
