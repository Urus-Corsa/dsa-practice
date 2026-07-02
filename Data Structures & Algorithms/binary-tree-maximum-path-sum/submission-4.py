# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """

        """
        if not root:
            return 0
        
        max_seen = root.val
    
        def dfs(r):
            nonlocal max_seen
            if not r:
                return float('-inf')
            
            left_sum = dfs(r.left)
            right_sum = dfs(r.right)
            
            subtrees_max = max(left_sum+r.val, right_sum+r.val)
            local_max = max(subtrees_max, r.val)
            tree_max = max(local_max, left_sum+r.val+right_sum)
            max_seen = max(tree_max, max_seen)
            
            return max(local_max,0)
        
        dfs(root)
        return max_seen
