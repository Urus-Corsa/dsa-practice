# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        # when performing the traversal from leaves to root (bottom up), the first node that we can reach both p and q from it
        is the LCA of those two nodes.
        
        # brute force: for every node from bottom to top perform a dfs from it, if we could reach both p an q that's LCA
        this will take O(n^2) time and O(n) space

        Optimal:
        after 6:30 mins of looking at the pics and playing around, i was able to understand the how to do this
        Since this is a BST, we can use its property of having unique vals and small left and higher values to narrow down the path 
        we should take during traversal. This is similar to binary search. At each node, we check with respect to p and q,
        if both are less or more than root, then we know they are both in either left subtree or both in right subtree.
        the moment we see a split at a node where one is strictly bigger and other is strictly smaller than current node that's answer.
        This way, we don't need to traverse entire tree we only make on movement decision at a time either left or either right
        until answer is found. This will take O(logn) time and if we do it iteratively it will take O(1) space
        """
        curr = root
        while curr:
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
            else:
                return curr
        