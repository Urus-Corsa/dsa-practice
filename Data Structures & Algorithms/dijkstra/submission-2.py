class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj = {}
        for i in range(n): 
            adj[i] = []
        # after the first setup loop -> adj = {0: [], 1,: [], ..., 4:[]}

        for s, d, w in edges:
            adj[s].append((w, d))
        # after the second setup loop -> adj = {0: [(10,1), (3,2)], 1,: [], ..., 4:[]}

        shortest_path = {}
        minHeap = [(0, src)]
        while minHeap:
            src_weight, src_vertex = heapq.heappop(minHeap)

            if src_vertex in shortest_path:
                continue
            shortest_path[src_vertex] = src_weight

            for neighbor in adj[src_vertex]:
                dst_weight, dst_vertex = neighbor[0], neighbor[1]
                if not dst_vertex in shortest_path:
                    heapq.heappush(minHeap, (src_weight+dst_weight, dst_vertex))
        
        if len(shortest_path) != n:
            for i in range(n):
                if not i in shortest_path:
                    shortest_path[i] = -1
        return shortest_path
        

