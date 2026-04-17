class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = defaultdict(list)
        for i in range(len(times)):
            source, target, time = times[i]
            adj_list[source].append((target, time))
        min_heap = [(0,k)] #time to node k, node k
        # nodes_reached = set()
        dist = [float('inf') for i in range(n+1)]
        while min_heap:
            time_to_node, node = heapq.heappop(min_heap)
            if dist[node] <= time_to_node:
                continue
            dist[node] = time_to_node
            n -= 1
            if n == 0:
                return time_to_node
            for neigh, time_to_neigh in adj_list[node]:
                heapq.heappush(min_heap, (time_to_node+time_to_neigh, neigh))
        return -1 

