# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        b.f: traverse both separately using same algo bfs or dfs for simplicity
        then generate traversal path list or string in level order (bfs), pre,in,post order (dfs) compare and return bool.
        Time: if n nodes in p and m nodes in q, traversals take O(n + m) which could be simplified to O(n) if they are equal in
        size, and comparison of lists take O(min(m,n)) which if equal also O(n). Space needed for dfs in worst case is max_height(p,q) for 
        recurssion stack, and for bfs max_width(p,q). If trees are balanced bfs queue would take more space closer to max_size(p,q), 
        if skewed (linked list) dfs call stack will grow as large as max_size(p,q)

        Optimal: do a double bfs and dfs (single pass, 2 in parallel and compare at each node in place), if mismatched, then return False
        and if finished with no mismatch return True.
        Time O(min_size(p,q)), space depending on algo worst case O(min_size(p,q))
        """
        if not p and not q:
            return True
        if (p and not q) or (q and not p):
            return False
        queue = deque([(p,q)])
        while queue:
            for _ in range(len(queue)):
                p_node, q_node = queue.popleft()
                if not p_node and not q_node:
                    continue
                if p_node.val != q_node.val:
                    return False
                if p_node.left and q_node.left:
                    queue.append((p_node.left, q_node.left))
                elif not p_node.left and not q_node.left:
                     queue.append((None, None))
                else:
                    return False
                if p_node.right and q_node.right:
                    queue.append((p_node.right, q_node.right))
                elif not p_node.right and not q_node.right:
                    queue.append((None, None))
                else:
                    return False
        return True

                

