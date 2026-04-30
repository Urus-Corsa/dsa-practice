class UnionFind:
    def __init__(self, nodesSet):
        self.parent = {}
        self.rank = {}
        for node in nodesSet:
            self.parent[node] = node
            self.rank[node] = 1
        
    def find(self, node):
        while node != self.parent[node]:
            self.parent[node] = self.parent[self.parent[node]]
            node = self.parent[node]
        return self.parent[node]

    def union(self, node1, node2):
        parent1, parent2 = self.find(node1), self.find(node2)
        if parent1 == parent2:
            return False
        if self.rank[parent1] > self.rank[parent2]:
            self.parent[parent2] = parent1
            self.rank[parent1] += self.rank[parent2]
        else:
            self.parent[parent1] = parent2
            self.rank[parent2] += self.rank[parent1]
        return True


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        verteciesSet = set()
        for edge in edges:
            u, v = edge[0], edge[1]
            if not u in verteciesSet:
                verteciesSet.add(u)
            if not v in verteciesSet:
                verteciesSet.add(v)
        uf = UnionFind(verteciesSet)
        for edge in edges:
            u, v = edge[0], edge[1]
            uf.union(u,v)
        components_set = set()
        for vertex in verteciesSet:
            this_vertex_parent = uf.find(vertex)
            n -= 1
            if this_vertex_parent in components_set:
                continue
            components_set.add(this_vertex_parent)
        return len(components_set) + n