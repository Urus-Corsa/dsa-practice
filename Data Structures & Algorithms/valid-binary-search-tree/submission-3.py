# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        approach that comes to mind here is dfs from root. When we are traversing we validate the left and right
        subtree if dfs passes (returns True for both side) then we know it's valid.
        This will take us O(n) if we have n nodes in the tree, and for a rather balanced tree we are looking at our recurssion call stack growth
        to be as much as the longest path aka hieght of the tree so O(h) and if the tree is skewed this could now become closer or equal to the n
        which includes all nodes so O(n) space in the worst case for skewed tree. We know that in this problem the max number of nodes is 1000
        So worst case scenario n = 1000 or O(1000)
        """
        def dfs(r, low, high):
            if not r:
                return True
            if not (low < r.val < high):
                return False
            left_valid = dfs(r.left, low, r.val)
            if not left_valid:
                return False
            right_valid = dfs(r.right, r.val, high)
            if not right_valid:
                return False
            return True
        
        return dfs(root, float('-inf'), float('inf'))