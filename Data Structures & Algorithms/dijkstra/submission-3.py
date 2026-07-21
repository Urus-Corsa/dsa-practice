import heapq
from collections import defaultdict
class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj_list = defaultdict(list)
        for v1, v2, weight in edges:
            adj_list[v1].append((v2,weight))
        dist = {node: -1 for node in range(n)}
        visited = set()
        dist[src] = 0
        pq = [(0,src)]
        while pq:
            dist_to, node = heapq.heappop(pq)
            if dist_to > dist[node] or node in visited:
                continue
            visited.add(node)
            dist[node] = dist_to
            for neigh, dist_to_neigh in adj_list[node]:
                if dist[neigh] == -1 or dist_to_neigh+dist[node] < dist[neigh]:
                    dist[neigh] = dist_to_neigh+dist[node]
                    heapq.heappush(pq, (dist[neigh], neigh))
        return dist
            