class Graph:
    
    def __init__(self):
        self.adjList = {}

    def addEdge(self, src: int, dst: int) -> None:
        if src in self.adjList:
            self.adjList[src].add(dst)
        else:
            neighbors = set()
            neighbors.add(dst)
            self.adjList[src] = neighbors
        if not dst in self.adjList:
            self.adjList[dst] = set()

    def removeEdge(self, src: int, dst: int) -> bool:
        if src in self.adjList and dst in self.adjList[src]:
            self.adjList[src].remove(dst)
            return True
        return False

    def hasPath(self, src: int, dst: int) -> bool:
        if dst in self.adjList[src]:
            return True
        q = deque()
        visited = set()
        q.append(src)
        visited.add(src)
        while q:
            for _ in range(len(q)):
                v = q.popleft()
                if v == dst:
                    return True
                visited.add(v)
                if v in self.adjList:
                    for neighbor in self.adjList.get(v, []):
                        if neighbor in visited:
                            continue
                        q.append(neighbor)
                        visited.add(neighbor)
                else:
                    continue
        return False
