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
        if not root:
            return True
        queue = deque()
        if root.left:
            queue.append((root.left, float('-inf'), root.val))
        if root.right:
            queue.append((root.right, root.val, float('inf')))
        while queue:
            node, lower_bound, upper_bound = queue.popleft()
            if not (lower_bound < node.val < upper_bound):
                return False
            if node.left:
                queue.append((node.left, lower_bound, node.val))
            if node.right:
                queue.append((node.right, node.val, upper_bound))
        return True