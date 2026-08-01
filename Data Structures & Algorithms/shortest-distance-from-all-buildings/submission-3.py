class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        """
        b.f: from every cell run bfs and get their travel time to each house then sum them up for that cell and take a global min. Once all travel times are calculated for all cells return min.
        If we have m*n cells, this means we need to run bfs for every m*n cells in the grid. So this means that the bfs itself that will cost us O(v+e)-> where we have 4 edges at most per V so constant, and v here is m*n it'd be O(m*n), so total time is O((m*n)^2) (in the worst case we need to visit every other cell from every cell).
        Space needed will also be limited to how big the queue can grow which would be at most O(m.n) in total.

        optimal: we can apply floyd warshall. We basically compute shortest distance to every other house
        [
        (2+3+4),(1+2+3),1
        2,(2+1+2),1
        (4+3+2),(3+2+1),1
        ]
        """
        dist = []
        for i in range(len(grid)):
            this_row = []
            for j in range(len(grid[0])):
                if grid[i][j] in [1,2]:
                    this_row.append((-1,-1))
                else:
                    this_row.append((0,0))
            dist.append(this_row)

        def bfs(row, col, house):
            queue = deque()
            queue.append((row, col))
            seen = set()
            seen.add((row,col))
            dist_traveled = 1
            while queue:
                for _ in range(len(queue)):
                    r, c = queue.popleft()
                    for dr, dc in [(0,1),(1,0),(-1,0),(0,-1)]:
                        nr, nc = dr + r, dc + c
                        if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 0 and not (nr, nc) in seen:
                            queue.append((nr,nc))
                            seen.add((nr,nc))
                            dist[nr][nc] = (dist[nr][nc][0]+dist_traveled, dist[nr][nc][1]+1)
                dist_traveled += 1

        house_count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    house_count += 1
                    bfs(i,j,house_count)
        print(dist)
        min_dist = float('inf')
        
        for i in range(len(dist)):
            for j in range(len(dist[0])):
                if dist[i][j][1] == house_count and dist[i][j][0] < min_dist:
                    min_dist = dist[i][j][0]

        return min_dist if min_dist != float('inf') else -1