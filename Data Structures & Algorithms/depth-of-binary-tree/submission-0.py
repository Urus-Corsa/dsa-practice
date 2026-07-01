from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        2 approaches here:
        1. dfs: visit all nodes from root, while counting each level as we go down, then return the max seen
        Time comp will be O(v) if we have v nodes in the tree. We will use recursion and the recursion call stack will grow as large as
        the max(depth)/max(height) of the tree, if tree is skewed this number could be as high as v.
        2. bfs: level order traversal. We are gonna use a queue, where we will start from the root. We wanna visit every node, and at each new level
        we increment the depth, at the end once we process the last popped node from the queue we have actually processed the tail of the longest
        path from the root where at that point our variable must be incremented to the correct depth/level of the tree.
        time comp, similar to dfs if we have v nodes, will be O(v) to visit all nodes
        space comp, will be dependent on the size of width of tree, and the queue could be as large as the max width which in the worst case we say O(v)
        """
        if not root:
            return 0
        queue = deque()
        queue.append(root)
        depth = 0
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            depth += 1
        return depth
        