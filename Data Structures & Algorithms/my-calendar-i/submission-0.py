class Node:
    def __init__(self, l_bound = None, r_bound = None, l_child = None, r_child = None):
        self.l_bound = l_bound
        self.r_bound = r_bound
        self.l_child = l_child
        self.r_child = r_child

class MyCalendar:
    def __init__(self):
        self.root = None

    def book(self, startTime: int, endTime: int) -> bool:
        tree_root = self.root
        if not tree_root:
            self.root = Node(l_bound = startTime, r_bound = endTime)
            return True
        def traverse(root):
            if not root:
                return True 
            if endTime <= root.l_bound:
                if root.l_child:
                    return traverse(root.l_child)
                else:
                    root.l_child = Node(l_bound = startTime, r_bound = endTime)
                    return True
            elif startTime >= root.r_bound:
                if root.r_child:
                    return traverse(root.r_child)
                else:
                    root.r_child = Node(l_bound = startTime, r_bound = endTime)
                    return True
            else:
                return False
        return traverse(tree_root)
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)