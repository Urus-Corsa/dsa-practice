class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = defaultdict(list)
        for i in range(len(times)):
            source, target, time = times[i]
            adj_list[source].append((target, time))
        min_heap = [(0,k)] #time to node k, node k
        nodes_reached = set()
        while min_heap:
            time_to_node, node = heapq.heappop(min_heap)
            if node in nodes_reached:
                continue
            nodes_reached.add(node)
            if len(nodes_reached) == n:
                return time_to_node
            for neigh, time_to_neigh in adj_list[node]:
                if not neigh in nodes_reached:
                    heapq.heappush(min_heap, (time_to_node+time_to_neigh, neigh))
        # if len(nodes_reached) != n:
        return -1 

