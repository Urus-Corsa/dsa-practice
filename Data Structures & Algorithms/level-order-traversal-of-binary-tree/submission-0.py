# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        we need to perform a bfs here to be able to get all nodes on the same level.
        Time needed is going to be O(n) to traverse entire tree if tree has n nodes, and space needed will be the size
        of the queue of bfs which is O(w) where if tree is balanced it could grow to max of O(n) and if skewed O(1)
        """
        if not root:
            return []
        queue = deque()
        queue.append(root)
        values = []
        while queue:
            this_level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                this_level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            values.append(this_level)
        return values
        