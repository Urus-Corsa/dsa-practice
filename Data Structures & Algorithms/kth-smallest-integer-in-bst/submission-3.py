# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        we need to enumerate the nodes in sorted (ascending) order and return the kth element from it

        #approach: Could traverse tree, starting from the left most leaf node, add its root, and then the right sibiling (right of the leaf node), this way add all nodes into a list.
        Then we can return kth node.

        with dfs or bfs we can perform the traversal we can correctly enumerate the nodes. If we assumed the size of tree is
        n (number of nodes in tree), and height of tree (longest root to leaf path) is h, using dfs the time needed will be O(n) and space comp will be O(h) where if tree is balanced
        h = logn and if tree is skewed  h = n. If we used bfs time is same (O(n)) and space if tree is balanced O(n) because of width, and skewed O(1).
        Additionally since we are adding all nodes into a list the list will grow to size n as well so another O(n) needed here
        for this time is O(n) and space is O(n+n)~O(n)

        optimal: using same traversal rather than adding to list, we can enumerate post order as during return ups, and stop on kth and return that node.
        """
        res = None

        def dfs(r):
            nonlocal k
            nonlocal res
            if not r:
                return
            dfs(r.left)
            if k == 0:
                return
            res = r.val
            k -= 1
            if k == 0:
                return
            dfs(r.right)
        
        dfs(root)
        
        return res