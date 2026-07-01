# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        the solution that comes to mind is that we wanna be able to compare each node at the same positions in both trees.
        So we can traverse the tree from root either with bfs or dfs, and the moment we see a node from tree that it's val == subtree.val
        we perform a double dfs and bfs from those two nodes, if matched completely then we return True if not we continue with the rest of the nodes.
        """
        def isMatch(root, sub_root):
            if not root and not sub_root:
                return True
            if not root or not sub_root:
                return False
            if root.val != sub_root.val:
                return False
            left_matched = isMatch(root.left, sub_root.left)
            if not left_matched:
                return False
            right_matched = isMatch(root.right, sub_root.right)
            if not right_matched:
                return False
            return True
        queue = deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            if node.val == subRoot.val:
                if isMatch(node, subRoot):
                    return True
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return False
