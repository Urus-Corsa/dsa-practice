# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        clarification: inverting here means to have the left and right child of every root swapped.
        can root be empty? yes.
        what would be the data type of the root values? ints
        can the values be negative? yes
        is there a possiblity that tree will always be balanced or skewed? No, could be mixed way
        do we know the estimate height, size, or width of trees? We know that the size is somewhere between 0 to 100 nodes, but no other information.


        approach: this can be done with a post order traversal so we go down a subtree all the way to have reached the leaf nodes
        then once we are at the root of the leaf nodes we swap the left and right child (even if null) and return up and do the same
        time comp, we can estimate this way, if size of the arr in the worst case is 100 then we know we need to visit all 100 nodes, so it will take us O(100) in the worst case, and generalized is O(n)
        the space needed is dominated by the recursion stack space, since it grows with every recursive call made until returned. Generaly, it is in O(h) where h is length of longest root to leaf path.
        If tree is skewed then h could be as large as 100 so O(100) in the worst case.
        
        This can also be done with a bfs in the level order mannner using a queue and iteratively. Time comp, same as dfs, O(n) and here worst case is O(100).
        Space dominated by queue size where it will grow to largest width of tree in max, so if we considered w as width it would be O(w) ~ O(n)
        """
        """
        dry run
        """
        if not root: #dfs base case and empty root edge case safte guard
            return None
        l_node = self.invertTree(root.left)
        r_node = self.invertTree(root.right)
        #post order traversal so get both l and r children
        #swap nodes
        tmp = root.left
        root.left = root.right
        root.right = tmp
        return root
