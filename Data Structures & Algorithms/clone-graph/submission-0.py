"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """
        1<->2<->3
        1<->0<->3
        In this problem, we need to create a clone of the graph that we
        receive the initial node of it. We know the value of each node can 
        be found in node.val, and a list of its neighbor nodes in node.neighbors
        We can solve this problem by starting with input node, creating its clone, 
        and looking at its neighbors that we need to clone. Now, if we have already created
        this neighbor before (we can maintain a dict (vals as keys->node refs)) of nodes that we have created
        to perform a check of having have created already or not. If yes we use the same if not we creat and store it
        Then we recursively dfs on the neighbors to make all connections as present in original graph.
        We also need to be careful to not get stuck in an infinite recursion with properly identifying those already processed (if in dict
        we don't need to dfs on it again we just make connection), since graph is undirected
        The time needed to perform this dfs would be O(V+E) where V = number of nodes/vertecies in this graph, and E is the number of edges.
        Since we know this graph is undirected, so we can expect up to V(V-1)/2 edges maximum if the graph is dense, so
        the traversal may take O(V+V^2) ~ O(V^2). The space needed has to do with dict that will store our nodes which will
        grow as large as number of our nodes O(V). Each node can possibly have edges with every other node, which would
        make a node.neighbors list to grow as large O(V-1) or O(V). So total space comp would be O(V)
        """
        if not node:
            return None
        processed_nodes = {}
        def dfs(n):
            n_copy = Node(n.val) #n_copy = Node obj(val = 1), n_copy = Node(0)
            processed_nodes[n_copy.val] = n_copy # processed_nodes {1: Node obj(val=1)}, {1: Node obj(val=1), 0: Node(0)}
            for neigh in n.neighbors: #  n.neighbors = [0,2], [1,3]
                neigh_node_copy = None
                if neigh.val in processed_nodes:
                    neigh_node_copy = processed_nodes[neigh.val]
                else:
                    dfs(neigh) # dfs(0)
                    neigh_node_copy = processed_nodes[neigh.val]
                n_copy.neighbors.append(neigh_node_copy)
        dfs(node)
        return processed_nodes[node.val]
