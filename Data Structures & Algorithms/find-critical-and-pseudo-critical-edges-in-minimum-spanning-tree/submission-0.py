class UnionFind:
    def __init__(self, numOfNodes):
        self.parents = [i for i in range(numOfNodes)]
        self.ranks = [1] * numOfNodes

    def find(self, node):
        while node != self.parents[node]:
            self.parents[node] = self.parents[self.parents[node]]
            node = self.parents[node]
        return self.parents[node]
    
    def union(self, node1, node2):
        parent1, parent2 = self.find(node1), self.find(node2)
        if parent1 == parent2:
            return False
        if self.ranks[parent1] > self.ranks[parent2]:
            self.parents[parent2] = parent1
            self.ranks[parent1] += self.ranks[parent2]
        else:
            self.parents[parent1] = parent2
            self.ranks[parent2] += self.ranks[parent1]
        return True
        
class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        for i in range(len(edges)):
            edges[i].append(i)
        edges.sort(key=lambda e: e[2])
        mst_weight = 0
        uf = UnionFind(n)
        for edge in edges:
            v1, v2, w, idx = edge
            if uf.union(v1, v2):
                mst_weight += w
        critical = []
        psuedo_critical = []
        for i in range(len(edges)):
            this_edge = edges[i]
            mst_weight2 = 0 
            uf2 = UnionFind(n)
            connected_count = 0
            for j in range(len(edges)):
                if i == j:
                    continue
                v1, v2, w, idx = edges[j]
                if uf2.union(v1, v2):
                    mst_weight2 += w
                    connected_count += 1
            if connected_count != n-1 or mst_weight2 > mst_weight:
                critical.append(this_edge[3])
                continue
            mst_weight2 = this_edge[2]
            uf2 = UnionFind(n)
            uf2.union(this_edge[0],this_edge[1])
            connected_count = 1
            for j in range(len(edges)):
                if i == j:
                    continue
                v1, v2, w, idx = edges[j]
                if uf2.union(v1, v2):
                    mst_weight2 += w
                    connected_count += 1
            if mst_weight2 == mst_weight:
                psuedo_critical.append(this_edge[3])
                
        return [critical, psuedo_critical]