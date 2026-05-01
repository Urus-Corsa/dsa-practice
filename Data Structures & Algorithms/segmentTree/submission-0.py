class Node:
    def __init__(self, l_bound = None, r_bound = None, l_child = None, r_child = None, sum_ = None):
        self.sum_ = sum_
        self.l_bound = l_bound
        self.r_bound = r_bound
        self.l_child = l_child
        self.r_child = r_child


class SegmentTree:    
    def __init__(self, nums: List[int]):
        
        def buildSegmentTree(l_ind, r_ind):
            root = Node(l_bound=l_ind, r_bound=r_ind)
            if l_ind == r_ind:
                root.sum_ = nums[l_ind]
                return root
            mid_point = (l_ind+r_ind)//2
            root.l_child = buildSegmentTree(l_ind, mid_point)
            root.r_child = buildSegmentTree(mid_point + 1, r_ind)
            root.sum_ = root.l_child.sum_ + root.r_child.sum_
            return root
        
        self.root = buildSegmentTree(0, len(nums)-1)

    def update(self, index: int, val: int) -> None:
        tree_root = self.root
        if not tree_root.l_bound <= index <= tree_root.r_bound:
            return 0
        
        def traverse(root):
            if not root:
                return 0
            if root.l_bound == root.r_bound:
                if index == root.l_bound:
                    root.sum_ = val
                return root.sum_
            # mid_point = (root.l_bound + root.r_bound)//2
            l_child_sum = traverse(root.l_child)
            r_child_sum = traverse(root.r_child)
            root.sum_ = l_child_sum + r_child_sum
            return root.sum_

        traverse(tree_root)

    
    def query(self, L: int, R: int) -> int:
        tree_root = self.root

        def getRangeSum(root):
            if not root:
                return 0
            if root.l_child == root.r_child:
                if L <= root.l_bound <= R:
                    return root.sum_
                return 0
            l_sum = getRangeSum(root.l_child)
            r_sum = getRangeSum(root.r_child)
            return l_sum+r_sum
        
        return getRangeSum(tree_root)
