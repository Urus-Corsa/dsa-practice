class UnionFind:
    def __init__(self, rows, cols):
        self.parent = [i for i in range(rows*cols)]
        self.rank = [0 for _ in range(rows*cols)]
        self.cols = cols

    def get_id(self, row, col):
        return row * self.cols + col
    
    def find(self, cell):
        while cell != self.parent[cell]:
            self.parent[cell] = self.parent[self.parent[cell]]
            cell = self.parent[cell]
        return self.parent[cell]
    
    def union(self, cell1, cell2):
        par1, par2 = self.find(cell1), self.find(cell2)
        if par1 == par2:
            return False
        if self.rank[par1] >= self.rank[par2]:
            self.parent[par2] = par1
            self.rank[par1] += self.rank[par2]
        else:
            self.parent[par1] = par2
            self.rank[par2] += self.rank[par1]
        return True


class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        """
        approach, own words: Given a grid with water, the land cells will be in positions array. We wanna know when each is inserted, how many islands we will have in total.

        Clarifying questions? Input always valid? Positions always inbound? Positions duplicated? Can any of the input values be null? Do we know the max size of the input grid and positions?
        here are your constraints Sina:
        Constraints:
        1 <= m, n, positions.length <= 10⁴
        1 <= m * n <= 10⁴
        positions[i].length == 2
        0 <= rᵢ < m
        0 <= cᵢ < n

        Seems like positions can be duplicated.
        Sample input and output from interviewer:
        Input: m = 3, n = 3, positions = [[0,0],[0,1],[1,2],[2,1]]
        Output: [1,1,2,3]

        brute force approach is to process each land addition at once
        so we create the water grid, mark each land position at once, and run count number of islands at each insertion
        which will result in scanning the entire grid (bfs/dfs) at every insertion to know number of islands
        time: if len(positions) is k and our grid has size m*n, then this will take O(k(m*n)) in the worst case to get counts
        (doing the full grid of size m*n traversal k times to get count of islands)
        Space needed for this is if we run bfs or dfs, each call would push the m*n cells into call stack or queue + O(k) space needed for result array = O(m*n) + O(k) ~ O(m*n)

        Efficient: Note: I recognized union find is most likely going to solve this early on when saw the probelm but couldn't see how in implementation it can solve it. Like I know I need to apply union find to a solution, and I can recognize whether it'd be useful or not on my own, but I struggle to apply it actually. Example, when the nodes/cells of the grid need to be looked at as connected and disconnected components to compute something I need to use union find however when it comes to applying it in practice I struggle to see how UF could actually solve the request in implementation. 

        After giving this to another llm it pointed out some common patterns where union find is usually applied.
        I am now thinking of this approach to solve this:
        I will begin with initializing the count to zero, and then insert the first position as a land and increment the count. Then for each 
        """
        uf = UnionFind(m,n)
        grid = [[0 for _ in range(n)] for _ in range(m)]
        dirs = [(-1,0),(0,-1),(1,0),(0,1)]
        islands = 0
        res = []
        
        for lands_count, inserted_position in enumerate(positions):
            r, c = inserted_position
            if grid[r][c] != 0:
                res.append(islands)
                continue
            islands += 1
            grid[r][c] = 1
            for dr, dc in dirs:
                nr, nc = dr+r, dc+c
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                    if uf.union(uf.get_id(r,c), uf.get_id(nr,nc)):
                        islands -= 1
            res.append(islands)
        return res


            
