class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        queue = deque()
        visited = set()
        queue.append((0,0))
        visited.add((0,0))
        length = 0
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                if (r,c) == (len(grid)-1,len(grid[0])-1):
                    return length
                neighbors = [(0,1),(1,0),(0,-1),(-1,0)]
                for dr, dc in neighbors:
                    nr = r + dr
                    nc = c + dc 
                    if not 0<=nr<len(grid) or not 0<=nc<len(grid[0]) or grid[nr][nc] == 1 or (nr, nc) in visited:
                        continue
                    queue.append((nr, nc))
                    visited.add((nr, nc))
            length += 1
        return -1