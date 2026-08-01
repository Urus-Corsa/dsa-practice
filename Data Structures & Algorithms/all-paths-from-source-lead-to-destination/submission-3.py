from collections import defaultdict, deque
class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        """
        we basically wanna traverse all paths from source, and confirm that they all go and finish on the destination node.
        This means that from destination there must not be any out going edges, and the graph should not contain a cycle.
        Also destination should be the only node with no edges.

        So 2 early terminations: 1. destination node has edges or 2. any other node but destination node does not have any edges. Hmm however i think that if there is another disconnected component that is unreachable from source we don't care about it. So checking if any other node does not have edges that is not destination node, does not correctly mean to return early.

        Approaches that come to mind: run bfs or dfs from source, and make sure that we land on dest and if we ever landed on any other node and have nowhere else to go then false if all paths lead to destination then return True
        The time comp would be O(V+E) for traversal where here V equals n at most and we will have at most 2V edges since this a directed graph So time comp here will be roughly O(V+2V) where it simplifies to O(V)
        space comp: We need space for adj_list, queue size (bfs), visited set. In this scenario adj_list would have at most n keys and each key could have 2(n-1) sized edge list so at most n*2(n-1) ~ O(n^2) + queue size at most n + visited set at most n which all simplifies to O(n^2) in the worst case
        
        Input: n = 3, edges = [[0,1],[0,2]], source = 0, destination = 2
        adj_list = {
            0:[1,2],
            1:[],
            2:[]
        }
        queue = [0]
        seen = [0]

        """
        adj_list = defaultdict(list)
        processed_edges = set()

        for u, v in edges:
            if not (u,v) in processed_edges:
                adj_list[u].append(v)
                processed_edges.add((u,v))
        
        if source == destination:
            return True if not source in adj_list and not destination in adj_list else False
    
        if adj_list[destination] or not adj_list[source]:
            return False
        
        def dfs(node, seen):
            if node in seen:
                return False
            if node != destination and not adj_list[node]:
                return False
            seen.add(node)
            for neigh in adj_list[node]:
                if not dfs(neigh, seen):
                    return False
            seen.remove(node)
            return True
        
        return dfs(source, set())

        
