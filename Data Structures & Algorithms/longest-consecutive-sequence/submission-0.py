class UnionFind:
    def __init__(self,arr):
        self.parent = {}
        self.rank = {}
        for n in arr:
            self.parent[n] = n
            self.rank[n] = 1
    
    def find(self,element):
        while element != self.parent[element]:
            self.parent[element] = self.parent[self.parent[element]]
            element = self.parent[element]
        return self.parent[element]
    
    def union(self, element1, element2):
        parent1, parent2 = self.find(element1), self.find(element2)
        if parent1 == parent2:
            return self.rank[parent1]
        if self.rank[parent1] > self.rank[parent2]:
            self.parent[parent2] = parent1
            self.rank[parent1] += self.rank[parent2]
            return self.rank[parent1]
        else:
            self.parent[parent1] = parent2
            self.rank[parent2] += self.rank[parent1]
            return self.rank[parent2]

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        seen_nums = set()
        uf = UnionFind(nums)
        max_length = 1
        for n in nums:
            if not n in seen_nums:
                seen_nums.add(n)
                if n-1 in seen_nums:
                    max_length = max(uf.union(n, n-1), max_length)
                if n+1 in seen_nums:
                    max_length = max(uf.union(n, n+1), max_length)
        return max_length